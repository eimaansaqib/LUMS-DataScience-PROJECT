from json import dump
import pandas as pd
from requests import get

ENDPOINT = "https://metacritic-api.azurewebsites.net/"
PLATFORM = "playstation-4"

data = pd.read_csv("../Video_games_esrb_rating.csv")
responses = []

for idx, title in enumerate(data["title"]):
    print(idx, title)
    responses.append(get(ENDPOINT,
                         params={"game_title": title, "platform": PLATFORM}
                         ).json())

with open("ps4.json", "w", encoding="UTF-8") as outfile:
    dump(responses, outfile)
