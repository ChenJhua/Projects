#coding:utf-8


class SpiderMiddleware(object):
    def process_request(self, request):
        print(u"请求正在经过爬虫中间件: {}".format(request.url))
        return request

    def process_item(self, item):
        print("Item正在经过爬虫中间件:")
        return item


