# -*- coding: utf-8 -*-
import scrapy
from ..items import ChoutiproItem

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://dig.chouti.com/']

    def parse(self, response):
        div_list=response.xpath('/html/body/main/div/div/div[1]/div/div[2]/div[1]/div')
        for div in div_list:
            title = div.xpath('.//div/div/div[1]/a/text()').extract_first()
            author = div.xpath('.//div/div/div[2]/div[1]/span[1]/span/text()').extract_first()
            item =ChoutiproItem()
            item['title'] = title
            item['author'] = author
            print(item['title'] )

            yield item


