# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class ImageItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection=table='images'#分别表示MongoDB存储的colloction名称和Mysql存储的表名称
    id=Field()
    url=Field()
    title=Field()
    thumb=Field()
