# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_currency(value):
    return value.replace('zł', '').replace('\n', '').strip()


def add_base_address(value):
    return 'https://www.doz.pl' + value if value is not '' else None


class PharmacyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_currency), output_processor=TakeFirst())
    link = scrapy.Field(input_processor=MapCompose(
        add_base_address), output_processor=TakeFirst())
