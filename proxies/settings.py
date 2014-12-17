# -*- coding: utf-8 -*-

# Scrapy settings for proxies project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os
import os.path

BOT_NAME = 'proxies'

SPIDER_MODULES = ['proxies.spiders']
NEWSPIDER_MODULE = 'proxies.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'proxies (+http://www.yourdomain.com)'

PROXY_LIST = os.environ.get('DEVKB_PROXY') or 'proxies.txt'
