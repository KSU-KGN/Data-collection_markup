# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

"""
Каждая строка должна соответствовать одному изображению и содержать URL изображения,
локальный путь к файлу (после загрузки), название и категорию.
"""
import scrapy

from itemloaders.processors import TakeFirst, MapCompose, Compose

class UnsplashparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())       # название фото
    category = scrapy.Field()                               # список категорий фото
    url = scrapy.Field(output_processor=TakeFirst())        # URL страницы фото
    photo = scrapy.Field(output_processor=TakeFirst())      # локальный путь к файлу (после загрузки)
    _id = scrapy.Field()
    print()
