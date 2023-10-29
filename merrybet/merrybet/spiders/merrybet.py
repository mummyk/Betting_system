import json
import scrapy


class Merrybet(scrapy.Spider):
    """Class for scraping merrybet data"""
    name = "merrybet"
    baseUrl = "https://m.merrybet.com"
    #category = f'/rest/market/categories/{categoryId}/events'
    #events =f'/rest/market/events/{eventId}'
    start_urls = [f'{baseUrl}/rest/market/categories']

    def parse(self, response):
        data = json.loads(response.body)
        # Extract the "categoryId" values
        category_ids = [item["categoryId"] for item in data["data"]]

        # Print the "categoryId" values
        print("Category IDs:", category_ids)
        yield data
