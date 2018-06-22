#coding:utf-8

import requests
import chardet

from ..http.response import Response
from ..utils.log import logger

class Downloader(object):

    def get_response(self, request):
        if request.method.upper() == "GET":
            res = requests.get(request.url, headers = request.headers, params = request.params)

        elif request.method.upper() == "POST":
            res = requests.post(request.url, headers = request.headers, data = request.data)
        else:
            raise Exception("Request method {} is not support".format(request.method))

        logger.info("[{}] <{}>".format(res.status_code, res.url))

        # 判断响应的编码
        encoding = chardet.detect(res.content)["encoding"]

        return Response(res.url, res.status_code, res.headers, res.content, encoding, request)

