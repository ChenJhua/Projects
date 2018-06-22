#coding:utf-8


from gevent.pool import Pool as BasePool

# 将Python底层的网络库，自动打个补丁，设计到网络操作时，变为异步的方式执行


class Pool(BasePool):
    def apply_async(self, func, args=None, kwds=None, callback=None):

        # 当程序调用apply_async是h，默认返回父类的apply_async来处理
        # Python2 和 3 都能用的，
        return BasePool().apply_async(func=func, args=args, kwds=kwds, callback=callback)

        #Python3 写法
        #return super().apply_async(func=func, args=args, kwds=kwds, callback=callback)

    def close(self):
        pass

