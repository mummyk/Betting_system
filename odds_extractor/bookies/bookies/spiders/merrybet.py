import json
import scrapy


class MerrybetSpider(scrapy.Spider):
    """Class for scraping merrybet data"""
    name = "merrybet"
    allowed_domains = ["m.merrybet.com"]
    baseUrl = "https://m.merrybet.com"
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
        for event in event_id:
            events = f'/rest/market/events/{event}'
            event_ids.append(events)
        yield from response.follow_all(event_ids, self.event_parse)

    def event_parse(self, response):
        """Get the event from the event id"""
        data = json.loads(response.body)

        # Check if category3Name contains "Outrights"
        if "Outrights" not in data["data"]["category3Name"]:
            item = {
                "time": data["data"]["eventStart"],
                "sportType": data["data"]["category1Name"],
                "country": data["data"]["category2Name"],
                "league": data["data"]["category3Name"],
                "teams": data["data"]["eventName"],
                "gameName": [item["gameName"] for item in data["data"]["eventGames"]],
                "outcomeName": [item["outcomeName"] for j in data["data"]["eventGames"] for item in j["outcomes"]],
                "outcomeOdds": [item["outcomeOdds"] for j in data["data"]["eventGames"] for item in j["outcomes"]],
            }

            yield item
