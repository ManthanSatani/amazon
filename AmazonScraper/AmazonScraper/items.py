# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ASIN = scrapy.Field()
    Title = scrapy.Field()
    Price = scrapy.Field()
    Brand = scrapy.Field()
    Stock = scrapy.Field()
    ShipBy = scrapy.Field()
    Category = scrapy.Field()
    Weight = scrapy.Field()

class AmazonScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ASINs = scrapy.Field()
