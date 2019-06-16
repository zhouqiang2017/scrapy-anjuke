# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjuItem(scrapy.Item):
    # define the fields for your item here like:
    href = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    house_type = scrapy.Field()
    property_fee = scrapy.Field()
    total_area = scrapy.Field()
    total_family = scrapy.Field()
    build_year = scrapy.Field()
    carport = scrapy.Field()
    plot_ratio = scrapy.Field()
    green_ratio = scrapy.Field()
    developer = scrapy.Field()
    tenement = scrapy.Field()
    business_district = scrapy.Field()
    summary = scrapy.Field()
    image = scrapy.Field()
