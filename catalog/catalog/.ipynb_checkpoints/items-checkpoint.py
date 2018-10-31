# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CatalogItem(scrapy.Item):
    
    catalogid = scrapy.Field()
    title = scrapy.Field()
    credits = scrapy.Field()
    attributes = scrapy.Field()
    coreqs = scrapy.Field()
    prereqs = scrapy.Field()
    fees = scrapy.Field()
    description = scrapy.Field()
    
    pass
