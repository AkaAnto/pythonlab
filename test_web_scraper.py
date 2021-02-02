import unittest
import pytest
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        return scrapy.Request(url='http://quotes.toscrape.com/page/1/', callback=self.parse)
        

    def parse(self, response):
        page = response.url.split("/")[-2]
        return response
        # filename = f'quotes-{page}.html'
        # with open(filename, 'a+') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')


class MyTest(unittest.TestCase):
    def test_method1(self):
        spider = QuotesSpider()
        response = spider.start_requests()
        print("hola ",response.css('title'))
        assert False, "Fail for example"