# -*- coding: utf-8 -*-
import scrapy
class QbproItem(scrapy.Item):

    author = scrapy.Field()
    content = scrapy.Field()

