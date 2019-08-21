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
        trs=etree.HTML(response.body).xpath('//table/tr[position()>1]')
        for tr in trs:
            try:
                res=tr.xpath('./td[position()>1]')
                ip=res[0].text
                port=res[1].text
                item = ProxyspiderItem(
                    ip=ip,
                    port=port
                )
                yield item
            except Exception as e:
                print(e)
        pass
    def start_requests(self):
        for i in range(100):
            url="{0}{1}".format(self.start_urls[0],i+1)
            yield scrapy.Request(url=url,callback=self.parse)