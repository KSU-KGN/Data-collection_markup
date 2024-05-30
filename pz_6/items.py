# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

"""
Определите элемент (Item) в Scrapy, который будет представлять изображение.
Ваш элемент должен включать такие детали,
как URL изображения, название изображения и категорию, к которой оно принадлежит.
"""

import scrapy

class UnsplashparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()
