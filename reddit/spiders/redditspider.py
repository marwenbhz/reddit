# -*- coding: utf-8 -*-
import scrapy


class RedditspiderSpider(scrapy.Spider):
    name = 'redditspider'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://www.reddit.com/']

    def parse(self, response):
        pass
