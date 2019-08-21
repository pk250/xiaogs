# -*- coding: utf-8 -*-
import requests
from lxml import etree

import scrapy

from proxyspider.items import ProxyspiderItem


class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/']

    def parse(self, response):
        trs=etree.HTML(response.body).xpath('//tbody/tr')
        for tr in trs:
            ip=tr.xpath('.//td[@data-title="IP"]')
            port=tr.xpath('.//td[@data-title="PORT"]')
            print("IP;{0},PORT:{1}".format(ip[0].text,port[0].text))
            item=ProxyspiderItem(
                ip=ip[0].text,
                port=port[0].text
            )
            yield item
        pass

    def start_requests(self):
        for x in range(100):
            #yield scrapy.Request(urljoin(self.start_urls[0],self.getUrl(x+1)),callback=self.parse)
            url="https://www.kuaidaili.com/free/inha/{0}/".format(x+1)
            print(url)
            yield scrapy.Request(url,callback=self.parse)