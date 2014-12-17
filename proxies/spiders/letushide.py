# -*- coding: utf-8 -*-
import scrapy

from proxies.settings import PROXY_LIST
from proxies.items import ProxyItem

class LetushideSpider(scrapy.Spider):
    name = "letushide"
    start_urls = ('http://letushide.com/protocol/http/',
                  'http://letushide.com/protocol/https/')
    allowed_domains = ('letushide.com',)
    fout = open(PROXY_LIST, 'w')

    def parse(self, response):
        for proxy in response.css('table#basic.data tbody tr'):
            item = ProxyItem()
            item['host'] = proxy.xpath('td[2]/a/text()').extract().pop()
            item['port'] = proxy.xpath('td[3]/text()').extract().pop()
            item['protocol'] = proxy.xpath('td[4]/a/text()').extract().pop()
            self.fout.write('%(protocol)s://%(host)s:%(port)s\n' % item)
            yield item
