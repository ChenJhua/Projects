#coding:utf-8


class Request(object):
    """
        框架的请求类，可以初始化请求对象数据
    """
    def __init__(self, url, method="GET", headers=None, params=None, data=None, callback="parse", spider=None, do_filter=True):
        self.url = url # 请求的url
        self.method = method  # 请求方法
        self.headers = headers  # 请求报头
        self.params = params  # 查询字符串
        self.data = data # 表单数据
        self.callback = callback # 指定回调函数，默认是parse
        self.spider = spider   # 请求对应的爬虫对象
        self.do_filter = do_filter # 请求去重处理
