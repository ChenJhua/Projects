#coding:utf-8


from scrapy_plus.core.engine import Engine

# # 导入爬虫类
# from spiders import BaiduSpider, DoubanSpider

# # 导入管道类
# from pipelines import BaiduPipeline, DoubanPipeline

# # 导入中间件类
# from middlewares import SpiderMiddleware1, SpiderMiddleware2, DownloaderMiddleware1, DownloaderMiddleware2

import time

if __name__ == "__main__":
    engine = Engine()
    while True:
        engine.start()
        time.sleep(5)

    # engine = Engine(baidu_spider)
    # engine.start()

    # engine = Engine(douban_spider)
    # engine.start()

    # spiders = {BaiduSpider.name : BaiduSpider(), DoubanSpider.name : DoubanSpider()}

    # pipelines = [BaiduPipeline(), DoubanPipeline()]

    # spider_mids = [SpiderMiddleware1(), SpiderMiddleware2()]
    # downloader_mids = [DownloaderMiddleware1(), DownloaderMiddleware2()]


    # engine = Engine(spiders, pipelines, spider_mids, downloader_mids)
    # engine.start()


    # print(BaiduSpider)
