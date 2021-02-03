import unittest
import pytest
import scrapy
from scrapy.crawler import CrawlerProcess
from scraper.qoutes import QuotesSpider
#pytest test_web_scraper.py





class MyTest(unittest.TestCase):
   
    def test_method1(self):
        process = CrawlerProcess(settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        })
        defer = process.crawl(QuotesSpider)
        # defer.addCallback(self.finished_callback)
        process.start()# the script will block here until the crawling is finished
        
        assert False, "Fail for example"