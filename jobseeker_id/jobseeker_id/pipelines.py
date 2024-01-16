# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class JobseekerIdPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            host='localhost',
            port=27017,
            username='admin',
            password='admin'
        )
        self.db = self.conn['jobseeker_id_db']
        self.collection = self.db['jobseeker_id']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
