# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from w3lib.html import remove_tags
from scrapy.loader.processors import MapCompose
from scrapy import Item


class NewsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_content = scrapy.Field(output_processor=lambda e: remove_tags((e[0])))
    article_url = scrapy.Field(output_processor=lambda e: e[0])
    author = scrapy.Field(output_processor=lambda e: e[0])
    title = scrapy.Field(output_processor=lambda e: e[0])
    word_count = scrapy.Field(output_processor=lambda e: e[0])
    lead_image_url = scrapy.Field(output_processor=lambda e: e[0])