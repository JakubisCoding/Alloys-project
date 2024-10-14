import scrapy


class MatwebSpiderSpider(scrapy.Spider):
    name = "matweb_spider"
    allowed_domains = ["matweb.com"]
    start_urls = ["https://matweb.com"]

    def parse(self, response):
        pass
