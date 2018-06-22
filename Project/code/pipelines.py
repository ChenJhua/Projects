#coding:utf-8


#管道、中间件 处理请求/响应/ITEM，不分爬虫！

from spiders import BaiduSpider, DoubanSpider

class BaiduPipeline(object):
    """
        区分只处理baiduspider的数据
    """
    def process_item(self, item, spider):
        if isinstance(spider, BaiduSpider):
            print(u"这是BaiduSpider的数据 : {}".format(item.data))
        return item


class DoubanPipeline(object):
    """
        区分只处理doubanspider的数据
    """
    def process_item(self, item, spider):
        if isinstance(spider, DoubanSpider):
            print(u"这是DoubanSpider的数据 : {}".format(item.data))
        return item

