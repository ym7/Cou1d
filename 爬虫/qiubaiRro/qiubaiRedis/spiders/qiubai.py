# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import QiubairedisItem
class QiubaiSpider(RedisCrawlSpider):
    name = 'qiubai'
    # allowed_domains = ['www.xx.cn']
    # start_urls = ['http://www.xx.cn/']
    redis_key = 'qiubai'

    rules = (
        Rule(LinkExtractor(allow=r'/8hr/page/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        li_list = response.xpath('//*[@id="content"]/div/div[2]/div/ul/li')
        for li in li_list:
            title = li.xpath('./div/a/text()').extract_first()
            author = li.xpath('./div/div/a/span/text()').extract_first()
            item = QiubairedisItem()
            item['title'] = title
            item['author'] = author

            yield item
