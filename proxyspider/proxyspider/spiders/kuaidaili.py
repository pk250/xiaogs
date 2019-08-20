# -*- coding: utf-8 -*-
import scrapy


class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/']

    def parse(self, response):
        pass
