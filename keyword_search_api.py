import config
import ssl

from pymongo import MongoClient
from sys import argv


def keyword_search(keyword):
	client = MongoClient(config.MONGODB_HOST, ssl_cert_reqs=ssl.CERT_NONE)
	db = client[config.MONGODB_DB_NAME]
	collection = db[config.MONGODB_COLLECTION]
	resp_list = collection.find({"$text":{"$search":keyword}})
	for resp in resp_list:
		print resp


if __name__ == '__main__':
	if len(argv) == 2:
		keyword_search(argv[1])
	else:
		print 'input parameter formate: "search text" '