import json
import os
from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


def read_data():
    # Specify the path to your JSON fileimport os

   # Get the base directory of the project
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # Move back one folder
    parent_dir = os.path.abspath(os.path.join(base_dir, os.pardir))
    json_file_path = f'{parent_dir}/data.json'

    # Open the file and load the JSON data
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Now 'data' contains the content of your JSON file
    return data


@app.get("/free")
def free():
    data = read_data()
    from datetime import datetime

    # Get the current date
    current_date = datetime.now()

    # Format the date as "Nov 21"
    formatted_date = current_date.strftime("%b %d")

    # Extract profit and bookmakers
    result = []
    for item in data:
        target_date_str = item["sport"]["startTime"]

        # Remove all commas from the string
        target_date_str_without_commas = target_date_str.split(",", 1)[0]
        print(f'Current date:- {formatted_date}')
        print(target_date_str_without_commas)
        if formatted_date == target_date_str_without_commas:
            entry = {
                "profit": {
                    "percentage": item["profit"]["percentage"],
                    "lifetime": item["profit"]["lifetime"]
                },
                "sport": {
                    "sportName": item["sport"]["sportName"],
                    "startTime": item["sport"]["startTime"]
                },
                "bookMakers": {}
            }
            for key, value in item["bookMakers"].items():
                entry["bookMakers"][key] = {
                    "bookmaker": value["bookmaker"],
                    #  "team_league": value["team_league"],
                    #  "odds_types": value["odds_types"],
                    #  "value": value["value"]
                }
            result.append(entry)

    return JSONResponse(content=result, media_type="application/json")


@app.get("/subscribed")
def subscribed():
    return
