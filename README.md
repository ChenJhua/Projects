# Projects
模仿Scrapy实现新框架Scrapy_plus,集setup安装、增量爬取、断点爬取、多线程、协程等功能


##[源码Github链接https://github.com/ChenJhua/Projects/tree/master/Project](https://github.com/ChenJhua/Projects/tree/master/Project)

###首先分析Scrapy的流程
![scrapy流程图](https://github.com/ChenJhua/GitHubImage/blob/master/GitHubImage/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20180701202457.png)

###从流程中抽取对象

 三个内置对象：

```
 请求对象(Request)
 响应对象(Response)
 数据对象(Item)
```

  五个核心组件：

```
 爬虫组件
     构建请求信息(初始的)，也就是生成请求对象(Request)
     解析响应对象，返回数据对象(Item)或者新的请求对象(Request)
 调度器组件
     缓存请求对象(Request)，并为下载器提供请求对象，实现请求的调度
     对请求对象进行去重判断
 下载器组件
     根据请求对象(Request)，发起HTTP、HTTPS网络请求，拿到HTTP、HTTPS响应，构建响应对象(Response)并返回
 管道组件
     负责处理数据对象(Item)
 引擎组件
     负责驱动各大组件，通过调用各自对外提供的API接口，实现它们之间的交互和协作
     提供整个框架的启动入口
```

  两个中间件：

```
 爬虫中间件
     对请求对象和数据对象进行预处理

 下载器中间件
     对请求对象和响应对象进行预处理
```

**五个核心模块和三个内置的对象是关键模块，需要优先实现**
**先抛开中间件，分析下它们之间的逻辑关系是：**
```
构造spider中start_urls中的请求
传递给调取器进行保存，之后从中取出
取出的request对象交给下载组件进行下载，返回response
response交给爬虫模块进行解析，提取结果
如果结果是request对象，重新交给调度器，如果结果是item对象，交给管道处理
```
**以上的逻辑是在引擎中完成的**
**对应的他们在引擎中的逻辑如下图：**

![这里写图片描述](https://github.com/ChenJhua/GitHubImage/blob/master/GitHubImage/snipaste_20180701_203405.png)

### 源码目录结构图
#####Project
![这里写图片描述](https://github.com/ChenJhua/GitHubImage/blob/master/GitHubImage/snipaste_20180701_204129.png)

####scrapy_plus
![这里写图片描述](https://github.com/ChenJhua/GitHubImage/blob/master/GitHubImage/snipaste_20180701_205034.png)

#### 具体实现看Github的代码，就不在这里复制粘贴了
