#coding:utf-8

import logging

# 默认的配置
DEFAULT_LOG_LEVEL = logging.INFO    # 默认等级
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'   # 默认日志格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
DEFAULT_LOG_FILENAME = 'log.log'    # 默认日志文件名称


ASYNC_COUNT = 16
#ASYNC_TYPE = "thread"
ASYNC_TYPE = "coroutine"


ROLE = None

# redis队列默认配置
REDIS_QUEUE_NAME = 'request_queue'
REDIS_QUEUE_HOST = 'localhost'
REDIS_QUEUE_PORT = 6379
REDIS_QUEUE_DB = 10


# redis的指纹集合配置
REDIS_SET_NAME = "fingerprint_set"
REDIS_SET_HOST = "localhost"
REDIS_SET_PORT = 6379
REDIS_SET_DB = 10

# 获取用户下的settings
from settings import *

