# -*- coding: utf-8 -*-
import scrapy

from proxies.settings import PROXY_LIST
from proxies.items import ProxyItem

http_urls = ['http://letushide.com/protocol/http/%d' % page for page in xrange(1, 20)]
https_urls = ['http://letushide.com/protocol/https/%d' % page for page in xrange(1, 20)]

class LetushideSpider(scrapy.Spider):
    name = "letushide"
    start_urls = http_urls + https_urls
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
