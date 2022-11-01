from json import dump
from time import sleep
import argparse
import pandas as pd
from requests import get


def get_data(game_title, platform, endpoint):
    """Get data from metacritic

    :param game_title: title of the game
    :type title: str
    :param platform: platform of the game
    :type platform: str
    :return: data from metacrictic
    :rtype: dict
    """
    try:
        res_json = get(endpoint, params={
            "game_title": game_title, "platform": platform}).json()

        res_json["name"] = game_title
        return res_json

    except ConnectionError:
        sleep(1)
        return get_data(title, platform, endpoint)


parser = argparse.ArgumentParser(description="Metacritic WebScraper")
parser.add_argument("platform", action="store", type=str,
                    help="metacritic platform identifier")
parser.add_argument("output", action="store",
                    type=str, help="output file name")

parsed_args = parser.parse_args()

ENDPOINT = "http://localhost:3000/"
DATASET_PATH = "../Video_games_esrb_rating.csv"
PLATFORM = parsed_args.platform
JSON_NAME = parsed_args.output

data = pd.read_csv(DATASET_PATH)
responses = []

for idx, title in enumerate(data["title"]):
    print(idx, title)
    responses.append(get_data(title, PLATFORM, ENDPOINT))

with open(JSON_NAME, "w", encoding="UTF-8") as outfile:
    dump(responses, outfile)
