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

from itemloaders.processors import TakeFirst, MapCompose, Compose

def process_name(value):
    value = value[0].strip()
    return value

def process_category(value):
    value = value[0].strip()
    return value

def process_photos(value:str):
    print()
    if value.startswith('//'):
        value = 'https:' + value.split()[0]
    else:
        value = value.split()[1]
    return value

class UnsplashparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=Compose(process_name), output_processor=TakeFirst())
    category = scrapy.Field(input_processor=MapCompose(process_category))
    url = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(process_photos))
    _id = scrapy.Field()

