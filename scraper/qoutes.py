import scrapy

#scrapy runspider qoutes.py

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        print(response.css('title::text'))