from json import dump
from time import sleep
import pandas as pd
from requests import get


def get_data(game_title, platform):
    """Get data from metacritic

    :param game_title: title of the game
    :type title: str
    :param platform: platform of the game
    :type platform: str
    :return: data from metacrictic
    :rtype: dict
    """

    try:
        res_json = get(ENDPOINT, params={
            "game_title": game_title, "platform": platform}).json()

        res_json["name"] = game_title
        return res_json

    except ConnectionError:
        sleep(1)
        return get_data(title, platform)


ENDPOINT = "https://metacritic-api.azurewebsites.net/"
PLATFORM = "playstation-4"
DATASET_PATH = "../Video_games_esrb_rating.csv"
JSON_NAME = "ps4.json"

data = pd.read_csv(DATASET_PATH)
responses = []

for idx, title in enumerate(data["title"]):
    print(idx, title)
    responses.append(get_data(title, PLATFORM))

with open(JSON_NAME, "w", encoding="UTF-8") as outfile:
    dump(responses, outfile)
