#coding:utf-8

from scrapy_plus.core.spider import Spider
from scrapy_plus.item import Item
from scrapy_plus.http.request import Request

class DoubanSpider(Spider):
    name = "douban"

    base_url = "https://movie.douban.com/top250?start="

    start_urls = [base_url + str(i) for i in range(0, 226, 25)]

    def parse(self, response):
        title_list = response.xpath("//span[@class='title'][1]/text()")


        yield Item(title_list)

        """
        # 提取详情页的链接并发送请求
        for link in response.xpath("//div[@class='hd']/a/@href"):
            yield Request(link, callback="parse_page")
        """

    def parse_page(self, response):
        """
            处理每个电影详情页的响应
        """
        yield Item(response.url)



class BaiduSpider(Spider):
    #start_url = "http://news.baidu.com/"
    name = "baidu"
    start_urls = [
        "http://www.baidu.com/",
        "http://news.baidu.com/",
        "http://www.baidu.com/",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, do_filter=False)

    def parse(self, response):
        title = response.xpath("//title/text()")[0]

        yield Item(title)

