import scrapy
from scrapy import signals
#scrapy runspider qoutes.py


class QuotesSpider(scrapy.Spider):
    name = 'signals'
    start_urls = ['http://quotes.toscrape.com/page/1/']
    items = []

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(QuotesSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(spider.finished, signal=signals.spider_closed)
        return spider

    def item_scraped(self, item):
        self.items.append(item)
        return item

    @staticmethod
    def finished(spider, reason):
        spider.log("FINISHED")
        spider.log(spider.items)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }