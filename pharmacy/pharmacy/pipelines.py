# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class PharmacyPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('pharmacy_items.db')
        self.coursor = self.conn.cursor()

    def create_table(self):
        # self.coursor.execute("""drop table if exists pharmacy_tb""")
        self.coursor.execute(""" create table if not exists pharmacy_tb(
            item_id INTEGER PRIMARY KEY,
            name TEXT,
            price TEXT,
            link TEXT,
            time TEXT
        )
        """)

    def store_db(self, item):
        self.coursor.execute("""insert into pharmacy_tb values (NULL, ?,?,?,?)""", (
            item['name'][0],
            item['price'][::],
            item['link'][::],
            item['time'][0]
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
