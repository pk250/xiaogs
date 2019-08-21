# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests


class ProxyspiderPipeline(object):
    def process_item(self, item, spider):
        ip,port=item.values()
        try:
            res = requests.get(url="http://icanhazip.com/", timeout=8,
                               proxies={"http": "{0}:{1}".format(ip, port)})
            if (ip[0].text == res.text):
                print("代理IP:{0},{1}".format(ip, "有效"))
                with open("proxy_ip.txt", 'a') as file:
                    file.write("{0}:{1}".format(ip, port))
            else:
                print("代理IP:{0},{1}".format(ip, "无效"))
        except:
            print("代理IP:{0},{1}".format(ip, "超时无效"))
        return item
