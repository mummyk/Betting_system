import json
import scrapy


class MerrybetSpider(scrapy.Spider):
    """Class for scraping merrybet data"""
    name = "merrybet"
    allowed_domains = ["m.merrybet.com"]
    baseUrl = "https://m.merrybet.com"
    # events =f'/rest/market/events/{eventId}'
    start_urls = [f'{baseUrl}/rest/market/categories']

    def parse(self, response):
        data = json.loads(response.body)
        # Extract the "categoryId" values
        category_ids = [item["categoryId"] for item in data["data"]]

        # Extarct all event ID values
        category_id = []
        for category in category_ids:
            category_url = f'{self.baseUrl}/rest/market/categories/{category}/events'
            category_id.append(category_url)
        yield from response.follow_all(category_id, self.category_parse)

    def category_parse(self, response):
        """Category Parsing function"""
        data = json.loads(response.body)
        # Extarct all event ID values
        event_ids = []
        # Extract the "eventId"
        event_id = [item['eventId'] for item in data['data']]
        item = {
            'event_id': data['data'][0]['eventId'],
            # Other fields
        }
        yield item
