import scrapy


class Merrybet(scrapy.Spider):
    """Class for scraping merrybet data"""
    name = "merrybet"
    baseUrl = "https://m.merrybet.com"
    start_urls = [f'{baseUrl}/rest/market/categories']

    def parse(self, response, **kwargs):
        yield "done"
