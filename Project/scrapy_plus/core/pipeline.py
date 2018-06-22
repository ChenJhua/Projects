#coding:utf-8


class Pipeline(object):
    def process_item(self, item, spider):
        print(u"Item : {}".format(item.data))
