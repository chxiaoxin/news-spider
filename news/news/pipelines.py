# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import ssl
import settings

from pymongo import MongoClient,TEXT

class NewsPipeline(object):

	def __init__(self):
		host_url = settings.MONGODB_HOST
		db_name = settings.MONGODB_DB_NAME
		collection_name = settings.MONGODB_COLLECTION
		client = MongoClient(host_url, ssl_cert_reqs=ssl.CERT_NONE)
		db = client[db_name]
		collection = db[collection_name]
		self.collection = collection
		self.collection.create_index([('article_content', TEXT)])

	def process_item(self, item, spider):
		object_id = self.collection.insert_one(dict(item))
		return item
