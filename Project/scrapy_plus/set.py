#coding:utf-8


import redis

from .conf.default_settings import *


class BaseFilterSet(object):
    def add_fp(self, fp):
        pass

    def is_filter(self, fp):
        pass


class NormalFilterSet(BaseFilterSet):
    """
        实现Python的set() 接口封装
    """
    def __init__(self):
        self._filter_set = set()

    def add_fp(self, fp):
        """
            将指纹添加到set中
        """
        self._filter_set.add(fp)

    def is_filter(self, fp):
        """
            判断指纹是否存在，如果存在返回True，表示是重复请求，否则返回False
        """
        return True if fp in self._filter_set else False

        # if fp in self._filter_set:
        #     return True
        # else:
        #     return False

class RedisFilterSet(BaseFilterSet):
    """
        实现Redis的set() 接口封装
    """


    def __init__(self):
        self._filter_set = redis.Redis(host=REDIS_SET_HOST, port=REDIS_SET_PORT, db=REDIS_SET_DB)
        self._key_name = REDIS_SET_NAME

    def add_fp(self, fp):
        """
            判断指纹是否存在，如果存在返回True，表示是重复请求，否则返回False
        """
        self._filter_set.sadd(self._key_name, fp)

    def is_filter(self, fp):
        """
            判断指纹是否存在，如果存在返回True，表示是重复请求，否则返回False
        """
        return self._filter_set.sismember(self._key_name, fp)







