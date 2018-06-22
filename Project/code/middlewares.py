#coding:utf-8


class SpiderMiddleware1(object):
    def process_request(self, request):
        print(u"请求正在经过爬虫中间件1: {}".format(request.url))
        return request

    def process_item(self, item):
        print("Item正在经过爬虫中间件1:")
        return item

class SpiderMiddleware2(object):
    def process_request(self, request):
        print(u"请求正在经过爬虫中间件2: {}".format(request.url))
        return request

    def process_item(self, item):
        print("Item正在经过爬虫中间件2:")
        return item




class DownloaderMiddleware1(object):
    def process_request(self, request):
        print(u"请求正在经过下载中间件1: {}".format(request.url))
        return request

    def process_response(self, response):
        print(u"响应正在经过下载中间件1: {}".format(response.url))
        return response

class DownloaderMiddleware2(object):
    def process_request(self, request):
        print(u"请求正在经过下载中间件2: {}".format(request.url))
        return request

    def process_response(self, response):
        print(u"响应正在经过下载中间件2: {}".format(response.url))
        return response



