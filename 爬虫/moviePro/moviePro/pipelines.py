# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MovieproPipeline(object):
    # fp =None
    # def open_spider(self,spider):
    #     print('start...')
    #     self.fp = open('./data.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        print(item)
        # self.fp.write(item['actor'].encode("gbk", 'ignore').decode("gbk", "ignore")+':'+item['title']+'\n')
        return item
    # def close_spider(self,spider):
    #     print('ending')
    #     self.fp.close()
