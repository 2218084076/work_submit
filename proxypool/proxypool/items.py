# Define here the models for your scraped items
# 保存爬取到的数据的容器
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxypoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip = scrapy.Field()
    country = scrapy.Field()
    post = scrapy.Field()

    pass
