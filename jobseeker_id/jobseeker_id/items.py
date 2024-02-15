# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobseekerIdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_link = scrapy.Field()

    job_desc = scrapy.Field()
    job_requirement = scrapy.Field()
    job_name = scrapy.Field()
    job_title = scrapy.Field()
    job_data = scrapy.Field()