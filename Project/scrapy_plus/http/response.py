#coding:utf-8

from lxml import etree
import re
import json

from ..utils.log import logger

class Response(object):
    """
        构建响应对象的类
    """
    def __init__(self, url, status_code, headers, body, encoding, request):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.encoding = encoding
        self.request = request


    def xpath(self, rule=""):
        """
            封装了xpath提取方法
        """
        html_obj = etree.HTML(self.body)
        return html_obj.xpath(rule)


    def re_findall(self, rule="", string=None):

        if string is None:
            string = self.body

        return re.findall(rule, string)

        # pattern = re.compile(rule)
        # result_list = pattern.findall(string)

        # re.findall(r"\d+", string)

        # response.re_findall(r"\d+")
    @property
    def json(self):
        try:
            return json.loads(self.body)
        except ValueError:
            logger.error("{} No JSON object could be decoded".format(self.url))

