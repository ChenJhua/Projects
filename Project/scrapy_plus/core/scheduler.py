#coding:utf-8

from ..conf.default_settings import *

# try:
#     from Queue import Queue
# except ImportError:
#     from queue import queue


# 做到接口兼容，判断是否是分布式，并使用对应的队列
# 如不是分布式模式，那么使用Python的Queue存储请求
if ROLE == None:
    # pip install six : 第三方模块，提供了py2和py3 模块的兼容问题
    from six.moves.queue import Queue
    from ..set import NormalFilterSet as Set
else:
    # 如果是分布式，就使用redis的队列
    from ..queue import Queue
    from ..set import RedisFilterSet as Set

from ..utils.log import logger

import w3lib.url
from hashlib import sha1
import six

class Scheduler(object):
    def __init__(self):
        self.queue = Queue()
        self._filter_set = Set()
        self.total_request = 0

    def add_request(self, request):
        """
            对请求去重，并添加到请求队列中
        """
        # 判断请求是否需要去重，如果不去重，直接添加请求到队列中，并返回，不再记录指纹
        if request.do_filter == False:
            logger.info("Add Request(don't filter): [{}] <{}>".format(request.method, request.url))
            self.queue.put(request)
            self.total_request += 1
            return

        # 获取请求指纹
        fp = self._get_fingerprint(request)

        # 判断该指纹的请求是否是重复请求
        if not self._filter_request(fp, request):
            logger.info("Add Reuqest: [{}] <{}>".format(request.method, request.url))
            # 如果不是重复请求，将请求放入请求队列
            self.queue.put(request)
            # 每次添加一个请求，计数器自增1
            self.total_request += 1
            # 并添加指纹到指纹集合中
            self._filter_set.add_fp(fp)


    def get_request(self):
        """
            胡群殴请求队列中的请求
        """
        try:
            # 如果队列为空，则抛出异常
            return self.queue.get(False)
        except:
            # 如果有异常，表示请求队列为空，返回None
            #logger.warning("Queue is empty!")
            return None



    def _filter_request(self, fp, request):
        if self._filter_set.is_filter(fp):
            logger.warning("{} filter.".format(request.url))
            return True
        else:
            return False


    def _get_fingerprint(self, request):
        """
            获取请求的指纹字符串
        """
        # 1. 将请求的url地址进行排序处理，并保存
        url = w3lib.url.canonicalize_url(request.url)

        # 2. 获取请求的method 的大写字符串
        method = request.method.upper()

        # 3. 处理查询字符串，进行排序处理，保证统一结果
        params = str(sorted(request.params.items(), key = lambda x : x[0])) if request.params else ""

        # 4. 处理表单数据，进行排序处理，保证统一结果
        data = str(sorted(request.data.items(), key = lambda x : x[0])) if request.data else ""

        s1 = sha1()
        s1.update(self._utf8_string(url))
        s1.update(self._utf8_string(method))
        s1.update(self._utf8_string(params))
        s1.update(self._utf8_string(data))

        # 返回sha1 的 字符串形式的 16进制数
        fp = s1.hexdigest()
        return fp



    def _utf8_string(self, string):
        """
            判断string是否是unicode字符串，如果是则返回该字符串的utf-8编码字符串
        """
        if six.PY2:
            if isinstance(string, unicode):
                return string.encode("utf-8")
            else:
                return string
        else:
            if isinstance(string, str):
                return string.encode("utf-8")
            else:
                return string









