# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from reddit.items import RedditItem

class RedditspiderSpider(scrapy.Spider):
    name = 'redditspider'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://www.reddit.com/r/pics/']
    custom_settings = {
    'LOG_FILE': 'logs/reddit.log',
    'LOG_LEVEL':'DEBUG'
     }
    rules = [
    	Rule(LinkExtractor(
    		allow=['/r/pics/\?count=\d*&after=\w*']),
    		callback='parse_item',
    		follow=True)
	]



    def parse(self, response):
        print('Processing...' + response.url)
        item = RedditItem()
	for pic in response.css('div.scrollerItem'):
	    item['link'] = response.urljoin(pic.css('div.imors3-1 > span > a.SQnoC3ObvgnGjWt90zD9Z::attr(href)').extract_first())
	    item['title'] = pic.css('div.imors3-1 > span > a.SQnoC3ObvgnGjWt90zD9Z > h2.imors3-0::text').extract_first()
	    item['author'] = pic.css('div.xvda30-0 > a._2tbHP6ZydRpjI44J3syuqC::text').extract_first().strip()
            item['comments'] = pic.css('span.FHCV02u6Cp2zYL0fhQPsO::text').extract_first()
	    yield item
