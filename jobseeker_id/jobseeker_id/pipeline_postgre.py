# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from psycopg2.extras import execute_batch
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# from ..conf import conf


class SeekPipeline(object):

    def __init__(self):
        #connect to db
        # credentials = conf.postgre_credential
        credentials = {
            'host': 'localhost',
            'port': 5432,
            'database': 'alcazar',
            'username': 'postgres',
            'password': 'postgres'
        }

        self.client = psycopg2.connect(
            host=credentials['host'],
            port=credentials['port'],
            database=credentials['database'],
            user=credentials['username'],
            password=credentials['password']
        )
        self.client.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.curr = self.client.cursor()

    def process_item(self, item, spider):
        self.store_db(
            item=item,
            table_name='seek'
        )
        return item
    
    def store_db(self, item, table_name):
        self.curr.execute(
            """insert into alcazar.public.seek(job_title, job_requirement, job_data, job_link) values (%s, %s, %s, %s)""", (
                item['job_title'][0],
                item['job_requirement'][0],
                item['job_data'][0],
                item['job_link']
            )
        )

    # def pg_insert(self, sql: str, data: list, page_size: int = 50):
    #     print(sql)
    #     return execute_batch(cur=self.cursor(), sql=sql, argslist=data, page_size=page_size)
    
    # def pg_insert_batch(self, data: list, schema_table: str, table_name: str, list_columns: list, column_values: str):
    #     values = "VALUES({})".format(",".join(["%s" for _ in list_columns]))
    #     insert_stmt = "INSERT INTO {} ({}) {}".format(schema_table + '.' + table_name, column_values, values)
    #     self.pg_insert(self.cursor(), insert_stmt)
        
    # def process_item(self, item, spider):
    #     #upsert query running

    #     #insert query running
    #     values = "VALUES({})".format(",".join(["%s" for _ in list_columns]))
    #     query_insert = "insert into {}.{}({}) values({})".format(schema_db, table_name, )
    
    #     self.client.execute()
        
'''
HW : 
1. gmn caranya import credential dan config lain dr file conf.py?

'''