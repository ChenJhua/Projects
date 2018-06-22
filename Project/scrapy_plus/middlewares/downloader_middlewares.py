#coding:utf-8



class DownloaderMiddleware(object):
    def process_request(self, request):
        print(u"请求正在经过下载中间件: {}".format(request.url))
        return request

    def process_response(self, response):
        print(u"响应正在经过下载中间件: {}".format(response.url))
        return response


