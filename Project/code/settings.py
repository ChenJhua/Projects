#coding:utf-8

DEFAULT_LOG_FILENAME = 'baidu.log'    # 默认日志文件名称



SPIDERS = [
    "spiders.BaiduSpider",
    #"spiders.DoubanSpider",
]

PIPELINES = [
    "pipelines.BaiduPipeline",
    #"pipelines.DoubanPipeline"
]

SPIDER_MIDDLEWARES = [
    #"middlewares.SpiderMiddleware1",
    #"middlewares.SpiderMiddleware2"
]

DOWNLOADER_MIDDLEWARES = [
    #"middlewares.DownloaderMiddleware1",
    #"middlewares.DownloaderMiddleware2"
]

# 并发量，默认是16个
#ASYNC_COUNT = 10

# 并发类型，默认是协程 (coroutine)
#ASYNC_TYPE = "thread"
#ASYNC_TYPE = "coroutine"


# 非分布式模式(默认)
ROLE = None

# 分布式模式
#ROLE = "slave" # 爬虫端
#ROLE = "master" # 服务器端

# redis队列默认配置
REDIS_QUEUE_NAME = 'request_queue'
REDIS_QUEUE_HOST = 'localhost'
REDIS_QUEUE_PORT = 6379
REDIS_QUEUE_DB = 10


# redis的指纹集合配置
# REDIS_SET_NAME = "fingerprint_set"
# REDIS_SET_HOST = "localhost"
# REDIS_SET_PORT = 6379
# REDIS_SET_DB = 10


