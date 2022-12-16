# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    
    title = scrapy.Field()
    date = scrapy.Field()
    score= scrapy.Field()
    genre = scrapy.Field()
    duree = scrapy.Field()
    description = scrapy.Field()
    acteurs = scrapy.Field()
    public = scrapy.Field()
    origine = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()

