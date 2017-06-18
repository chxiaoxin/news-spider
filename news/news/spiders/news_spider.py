# -*- coding: utf-8 -*-
import sys
import json
import requests

from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news.items import NewsItem

class NewsSpider(CrawlSpider):
    name = 'news_spider'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['https://www.theguardian.com/']

    rules=(
    	Rule(LinkExtractor(allow=(r'https://www.theguardian.com/\w+/\d+/\w+/\d+/[\w-]+')),callback='parse_item', follow=True),
    	)

    def parse_item(self, response):
    	mecury_url = 'https://mercury.postlight.com/parser?url='
    	mecury_headers = {'Content-Type':'application/json',
    				 	  'x-api-key':'P3qDxAQKNupO4422SsdCPFMnCYq3HoK9svTK55nI'
    					 }
    	l = ItemLoader(item = NewsItem(), response = response)
        parsed_article_resp = requests.get(mecury_url + response.url, headers=mecury_headers).text
        json_data = json.loads(parsed_article_resp)
        l.add_value('article_content', json_data['content'])
        l.add_value('article_url', json_data['url'])
        l.add_value('author', json_data['author'])
        l.add_value('title', json_data['title'])
        l.add_value('word_count', json_data['word_count'])
        l.add_value('lead_image_url', json_data['lead_image_url'])
        return l.load_item()