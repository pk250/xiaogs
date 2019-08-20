# -*- coding: utf-8 -*-
import requests
from lxml import etree

import scrapy



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
            try:
                res=requests.get(url="http://icanhazip.com/",timeout=8,proxies={"http":"{0}:{1}".format(ip[0].text,port[0].text)})
                if (ip[0].text==res.text):
                    print("代理IP:{0},{1}".format(ip[0].text, "有效"))
                else:
                    print("代理IP:{0},{1}".format(ip[0].text, "无效"))
            except:
                print("代理IP:{0},{1}".format(ip[0].text, "无效"))
        pass

    def start_requests(self):
        for x in range(100):
            #yield scrapy.Request(urljoin(self.start_urls[0],self.getUrl(x+1)),callback=self.parse)
            url="https://www.kuaidaili.com/free/inha/{0}/".format(x+1)
            print(url)
            yield scrapy.Request(url,callback=self.parse)