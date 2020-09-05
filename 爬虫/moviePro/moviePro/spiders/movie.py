# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieproItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.xx.cn']
    start_urls = ['https://www.4567kan.com/frim/index1.html']

    def detail_parse(self,response):
        item = response.meta['item']
        actor = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[3]/a/text()').extract_first()

        item['actor'] = actor

        yield item
    def parse(self, response):
        li_list = response.xpath('//li[@class="col-md-6 col-sm-4 col-xs-3"]')
        for li in li_list:
            item=MovieproItem()
            title = li.xpath('./div/a/@title').extract_first()
            detail_url = 'https://www.4567kan.com'+li.xpath('./div/a/@href').extract_first()
            item['title'] = title

            yield scrapy.Request(url=detail_url,callback=self.detail_parse,meta={'item':item})

