# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from ..items import WangyiproItem
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xx.com']
    start_urls = ['http://war.163.com/']
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='D:\迅雷下载\开发工具\chromedriver1.exe')



    def detail_parse(self,response):
        item = response.meta['item']
        content = response.xpath('//*[@id="endText"]/p[4]/text()').extract_first()
        item['content'] = content

        yield item
    def parse(self, response):
        div_list = response.xpath('//div[@class="data_row news_article clearfix "]')
        for div in div_list:
            # while enumerate(div_list) == 10:
            #     break
            item = WangyiproItem()

            title = div.xpath('.//div/div[1]/h3/a/text()').extract_first()
            print(title)
            detail_url = div.xpath('.//div/div[1]/h3/a/@href').extract_first()
            item['title'] = title

            yield scrapy.Request(url=detail_url,callback=self.detail_parse,meta={'item':item})
    def closed(self,spider):
        print('关闭浏览器对象')
        self.bro.quit()
