# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import mysql.connector


class WebscrapePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Kumar@pravin 007',
            database='mydb'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                            text text,
                            author text,
                            tags text
                            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb value(%s,%s,%s)""", (
            item['text'][0],
            item['author'][0],
            item['tags'][0]
        ))
        self.conn.commit()
