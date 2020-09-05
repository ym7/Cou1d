# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from redis import Redis

class WangyiproPipeline(object):
    fp = None
    def open_spider(self,spider):
        print('创建文件句柄')
        self.fp = open('./news_data.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        # print('执行写入')
        self.fp.write('标题: '+item['title']+'内容: '+item['content']+'\n')
        return item

    def close_spider(self,spider):
        print('写入完成')
        self.fp.close()


class RedierPipeline(object):
    conn = None
    def process_item(self,item,spider):
        self.conn = Redis(host='localhost',port=27017)
        data = {
            '标题':item['title'],
            '内容':item['content'],
        }
        self.conn.set('news',json.dumps(data))

        return item
