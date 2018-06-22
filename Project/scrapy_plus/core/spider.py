#coding:utf-8

#from scrapy_plus.http.request import Request
from ..http.request import Request
from ..item import Item


class Spider(object):
    """
        提供的Spider类，做为程序的入口
    """

    #start_url = "http://www.baidu.com"
    start_urls = []

    def start_requests(self):
        #start_requests = []
        if self.start_urls:
            for url in self.start_urls:
                yield Request(url)
        else:
            raise Exception("start_urls cant't by empty!")

        #return start_requests

    def parse(self, response):
        raise Exception("parse cant't by empty!")
        #return Request()
