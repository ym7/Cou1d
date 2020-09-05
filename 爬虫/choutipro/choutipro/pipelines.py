# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ChoutiproPipeline(object):
    fp = None
    def open_spider(self,spider):
        print("开始爬虫。。。。")
        self.fp =open('./data.text','w',encoding='utf-8')
    def process_item(self, item, spider):
        self.fp.write('作者:'+item['author']+'标题:'+item['title']+'\n')
        return item
    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()