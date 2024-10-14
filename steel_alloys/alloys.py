import scrapy

class MatwebSpider(scrapy.Spider):
    name = 'matweb_spider'
    allowed_domains = ['matweb.com']
    start_urls = ['https://www.matweb.com/search/PropertySearch.aspx']

    def parse(self, response):
        # Extract links to specific alloy data pages
        alloy_links = response.css('a::attr(href)').getall()
        for link in alloy_links:
            # Follow each alloy link and parse the alloy data
            yield response.follow(link, callback=self.parse_alloy)

    def parse_alloy(self, response):
        # Extract data from the alloy page
        alloy_name = response.css('h1::text').get().strip()
        composition = response.css('table#composition-table td::text').getall()
        properties = response.css('table#property-table td::text').getall()

        # Store data in dictionary format
        alloy_data = {
            'alloy_name': alloy_name,
            'composition': composition,
            'properties': properties
        }

        # Yield the data to store in JSON
        yield alloy_data
