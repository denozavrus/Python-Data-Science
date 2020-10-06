# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuotetutItem(scrapy.Item):

    image_url = scrapy.Field()
    sizes = scrapy.Field()
    styles = scrapy.Field()
    material = scrapy.Field()
    product_type = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()


