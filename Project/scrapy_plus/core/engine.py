#coding:utf-8

#from .spider import Spider
from .scheduler import Scheduler
from .downloader import Downloader
#from .pipeline import Pipeline

from ..http.request import Request
from ..item import Item

#from ..middlewares.spider_middlewares import SpiderMiddleware
#from ..middlewares.downloader_middlewares import DownloaderMiddleware
# 导入单例的logger对象
from ..utils.log import logger
from ..conf.default_settings import *


#多线程: threading.Thread,
# 注意：涉及到系统调度，多进程和多线程处理机制可能不一样（Linux），可以通过协程来替换

# 这是多进程模块里的多线程，Pool就是线程池，用法和多进程相同


# 封装协程Pool，做到接口兼容处理
if ASYNC_TYPE == "coroutine":
    from ..async.coroutine import Pool
elif ASYNC_TYPE == "thread":
    from multiprocessing.dummy import Pool
else:
    raise TypeError("{} types are not supported, must be 'thread' or 'coroutine'.".format(ASYNC_TYPE))

from datetime import datetime
import time

from gevent.monkey import patch_all
patch_all()
# # 使用协程池
# from gevent.pool import Pool
# from gevent.monkey import patch_all
# patch_all()




class Engine(object):
    def __init__(self, spiders={}, pipelines=[], spider_mids=[], downloader_mids = []):
        #self.spider = spider
        self.spiders = self._auto_import_instances(SPIDERS, True)
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipelines = self._auto_import_instances(PIPELINES)

        self.spider_mids = self._auto_import_instances(SPIDER_MIDDLEWARES)
        self.downloader_mids = self._auto_import_instances(DOWNLOADER_MIDDLEWARES)

        # 创建一个线程池
        self.pool = Pool()
        self.total_response = 0
        self.is_runing = True

    def _auto_import_instances(self, path=[], isspider=False):

        # 判断当前操作的是否是Spider，并初始化一个字典/列表，用来保存实例化对象
        if isspider:
            instances = {}
        else:
            instances = []

        import importlib

        for s in path:
            #each_path.split(".")
            # 根据字符串切片，获取模块名
            module_name = s[:s.rfind(".")]
            # 根据字符串切片，找到类名
            cls_name = s[s.rfind(".") + 1 :]

            # 根据模块名，获取该模块的绝对路径
            result = importlib.import_module(module_name)
            # 根据模块的绝对路径，获取模块内指定的类对象（不是实例化对象）
            cls_obj = getattr(result, cls_name)

            if isspider:
                # 如果是Spider，就生成Spider类实例化对象，并保存到字典中
                instances[cls_obj.name] = cls_obj()
            else:
                # 如果不是Spider，就生成Pipeline、Middlewares的实例化对象，并保存到列表中
                instances.append(cls_obj())

        # 最后返回字典/列表
        return instances


    def start(self):
        """
            提供外部的访问接口，启动引擎
        """
        start = datetime.now()
        logger.info("start time : {}".format(start))

        self._start_engine()
        stop = datetime.now()
        logger.info("stop time : {}".format(stop))

        # 统计两个时间差的秒数
        time = (stop - start).total_seconds()
        logger.info("useing time : {}".format(time))


    def _start_engine(self):

        if ASYNC_TYPE == "coroutine":
            logger.info("Coroutine is work!")
        else:
            logger.info("Thread is work!")

        if ROLE == "master" or ROLE == None:
            # 子线程工作
            if ROLE == "master":
                logger.info("Master is work!")
            self.pool.apply_async(self._execute_start_request)

        if ROLE == "slave" or ROLE == None:
            if ROLE == "slave":
                logger.info("Slave is work!")
            # 在外部控制子线程的数量
            for i in range(ASYNC_COUNT):
                # 子线程工作
                # 通过回调执行callback
                self.pool.apply_async(self._execute_request_response_item, callback = self._callback)

        while True:
            # 暂停一下，避免CPU疯狂空转
            time.sleep(0.01)
            # 当响应计数器和请求计数器相等时，表示所有请求处理结束（同时响应不为0表示避免一开始就break）
            if self.total_response == self.scheduler.total_request and self.total_response != 0:
                # 响应全部处理完毕，递归不需要再执行
                self.is_runing = False
                break

        # 关闭线程池，不再添加线程任务
        self.pool.close()
        # 子线程全部执行结束，通知主线程结束
        self.pool.join()

        logger.info("Main Thread is over!")


    def _callback(self, _):
        if self.is_runing:
            # 只要条件成立，一直递归调用自身，执行_execute_request_response_item
            self.pool.apply_async(self._execute_request_response_item, callback=self._callback)


    def _execute_start_request(self):
        #[("baidu", baidu_spider), ("douban", douban_spider)]
        for spider_name, spider in self.spiders.items():
            # 1. Spider返回第一个入口请求
            #start_requests = self.spider.start_requests()
            # 1. 获取生成器中的每个请求，并做处理
            for start_request in spider.start_requests():
                start_request.spider = spider

                for spider_mid in self.spider_mids:
                    # 2. 请求经过爬虫中间件做预处理并返回
                    start_request = spider_mid.process_request(start_request)

                # 3. 将预处理后的请求交给调度器处理
                self.scheduler.add_request(start_request)

    def _execute_request_response_item(self):
        #while True:
        # 4. 从调度器中获取一个请求
        request = self.scheduler.get_request()

        # 5. 判断请求是否为None，如果返回的Request是None，则表示队列为空，退出循环
        if request is None:
            return
        # 获取请求对象的爬虫对象
        spider = request.spider

        # 5. 将请求交给下载器下载之前，奥给下载中间件做预处理并返回
        for downloader_mid in self.downloader_mids:
            request = downloader_mid.process_request(request)

        # 6. 将预处理后请求交给下载器下载，并返回响应
        response = self.downloader.get_response(request)

        # 7. 将响应交给下载中间件做预处理并返回
        for downloader_mid in self.downloader_mids:
            response = downloader_mid.process_response(response)

        # 8. 将响应交给爬虫解析，并返回 Item 或 Request
        #item_or_requests = self.spider.parse(response)
        #parse_func = self.spider.parse(response):

        # 查找Spider对象包含的 请求的callback，并返回该回调函数
        parse_func = getattr(spider, request.callback)

        # 将响应做为参数传给callback，parse_func就是一个可迭代的生成器
        for item_or_request in parse_func(response):
            # 7. 判断Item 或 Request，并做对应处理，处理结束进入下一个while 循环
            if isinstance(item_or_request, Request):
                item_or_request.spider = request.spider
                request = item_or_request

                # 7.1 如果是请求对象，则通过爬虫中间件做预处理，再交给调度器
                for spider_mid in self.spider_mids:
                    request = spider_mid.process_request(request)

                self.scheduler.add_request(request)

            elif isinstance(item_or_request, Item):
                # 7.2 如果是Item对象，则通过爬虫中间件做预处理，再交给管道

                item = item_or_request

                for spider_mid in self.spider_mids:
                    item = spider_mid.process_item(item)

                for pipeline in self.pipelines:
                    item = pipeline.process_item(item, spider)
                # 所有管道处理完后，删除item对象（交还内存空间）
                del(item)
            else:
                # 如果不是Request也不是Item，则抛出异常
                raise ValueError("Data type is not support.")

        # 每次处理完一个响应，计数器自增1 （对应Scheduler的请求计数器）
        self.total_response += 1
