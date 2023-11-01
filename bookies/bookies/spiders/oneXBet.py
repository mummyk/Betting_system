import json
import scrapy


class OneXBetSpider(scrapy.Spider):
    """Class for scraping OneXBet data"""
    name = "oneXBet"
    allowed_domains = ["1xbet.ng"]
    baseUrl = "https://1xbet.ng"
    # event_url = "https://1xbet.ng/LineFeed/GetGameZip?id=186290641&lng=en&tzo=-7&isSubGames=true&GroupEvents=true&countevents=50&partner=159&grMode=2&country=132&marketType=1&mobi=true"
    start_urls = [
        f'{baseUrl}/LineFeed/GetSportsShortZip?sports=40&lng=en&country=132&partner=159&gr=354']

    def parse(self, response):
        data = json.loads(response.body)
        import datetime

        timestamp = 1698867000
        human_readable_date = datetime.datetime.utcfromtimestamp(timestamp)

        print(human_readable_date)

        formatted_date = human_readable_date.strftime("%Y-%m-%d %H:%M:%S")
        print('Formatted Time', formatted_date)

        yield data

      # yield from response.follow_all(category_id, self.category_parse)

  #  def category_parse(self, response):
  #      """Category Parsing function"""
  #      data = json.loads(response.body)
  #      # Extarct all event ID values
  #      event_ids = []
  #      # Extract the "eventId"
  #      event_id = [item['eventId'] for item in data['data']]
  #      for event in event_id:
  #          events = f'/rest/market/events/{event}'
  #          event_ids.append(events)
  #      yield from response.follow_all(event_ids, self.event_parse)

  #  def event_parse(self, response):
  #      """Get the event from the event id"""
  #      data = json.loads(response.body)

  #      # Check if category3Name contains "Outrights"
  #      if "Outrights" not in data["data"]["category3Name"]:
  #          item = {
  #              "time": data["data"]["eventStart"],
  #              "sportType": data["data"]["category1Name"],
  #              "country": data["data"]["category2Name"],
  #              "league": data["data"]["category3Name"],
  #              "teams": data["data"]["eventName"],
  #              "gameName": [item["gameName"] for item in data["data"]["eventGames"]],
  #              "outcomeName": [item["outcomeName"] for j in data["data"]["eventGames"] for item in j["outcomes"]],
  #              "outcomeOdds": [item["outcomeOdds"] for j in data["data"]["eventGames"] for item in j["outcomes"]],
  #          }

  #          yield item
