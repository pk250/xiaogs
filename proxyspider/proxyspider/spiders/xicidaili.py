# -*- coding: utf-8 -*-
from lxml import etree

import scrapy

from proxyspider.items import ProxyspiderItem
from scrapy import Selector


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/']

    def parse(self, response):
        selector=Selector(response)
        trs =selector.xpath('//table/tr')
        for tr in trs:
            res=tr.xpath('.//td').extract()
            ip=res[1].text
            port=res[1].text
            item = ProxyspiderItem(
                ip=ip,
                port=port
            )
            yield item
        pass
    def start_requests(self):
        for i in range(100):
            url="{0}{1}".format(self.start_urls[0],i)
            yield scrapy.Request(url=url,callback=self.parse)