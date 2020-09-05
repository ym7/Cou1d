# -*- coding: utf-8 -*-
import scrapy
from ..items import ModelsItem

class XxxSpider(scrapy.Spider):
    name = 'xxx'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.meitulu.com/item/4150.html']
    url  = 'https://www.meitulu.com/item/4150_%d.html'
    pageNum = 2

    def parse(self, response):
        img_url_list = response.xpath('/html/body/div[4]/center/img/@src').extract()
        for img_url in img_url_list:
            item = ModelsItem()
            item['src'] = img_url
            yield item

            if self.pageNum <=26:
                self.pageNum+=1
                url = format(self.url%self.pageNum)

                yield scrapy.Request(url=url,callback=self.parse)

