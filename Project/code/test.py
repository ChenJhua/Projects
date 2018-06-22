#coding:utf-8


import redis

client = redis.Redis(db=10)

name = "fp_set"
data1 = "hello"
data2 = "world"
data3 = "hello"

client.sadd(name, data3)

result = client.sismember(name, "hello123")
print(result)








# import redis

# from scrapy_plus.http.request import Request

# import pickle
# # pickle.dumps() : 将python对象，转为一个二进制数据
# # pickle.loads() : 将通过dumps()转为的二进制数据，转回Python对象


# client = redis.Redis(db=5)

# name = "queue"
# #data = "hello world!"
# #data = Request("http://www.baidu.com/")
# # 将请求对象，转为二进制数据
# data = pickle.dumps(Request("http://www.baidu.com/"))

# print(data)
# print(type(data))
# #lpush + rpop
# #rpush + lpop

# client.lpush(name, data)

# s = client.rpop(name)
# # 将数据库里的二进制数据，再转回为一个请求对象，之后可以发送出去
# r = pickle.loads(s)

# print(r)
# print(r.callback)
# print(type(r))






# import settings

# print(settings.SPIDERS)

# print(settings.PIPELINES)

# print("--" * 20)

# # 处理模块导入相关操作
# import importlib


# # 参数是一个和模块名，返回该模块所在的绝对路径
# path = importlib.import_module("spiders")
# print(path)

# print("-----" * 20)

# # 根据实例化对象，返回该对象指定的属性
# # 根据模块的绝对路径，返回指定类的类对象
# cls_obj = getattr(path, "BaiduSpider")
# print(cls_obj)



