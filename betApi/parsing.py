from bs4 import BeautifulSoup

with open('saved_page.html', 'r', encoding='utf-8') as file:
    files = file.read()
saved_html = files
soup = BeautifulSoup(saved_html, 'lxml')
datas = (soup.find_all('tbody'))
parsed_data = {}
for i in datas:

    percentage = i.find('div', class_='percent').text
    lifetime = i.find('div', class_='lifetime').text
    sportName = i.select_one('.sport .percent').text
    startTime = i.select_one('.sport .lifetime span').text
    bookies_data = {}

    for index, row in enumerate(i.find_all('tr', class_='odd_row'), start=1):
        bookie_data = {
            'bookmaker': row.select_one('.bookmaker_td').text.strip(),
            'team_league': row.select_one('.team_league_td .liga').text.strip(),
            'odds_types': row.select_one('.odds_types').text.strip(),
            'value': row.select_one('.values').text.strip()
        }
        bookies_data[index] = bookie_data

    parsed_data = {
        "profit": {
            "percentage": percentage,
            "lifetime": lifetime
        },
        "sport": {
            "sportName": sportName,
            "startTime": startTime
        },
        "bookMakers": bookies_data
    }
    print(parsed_data)
    # print(i)
