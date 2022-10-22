# Metacritic API

- [Metacritic API](#metacritic-api)
- [Installation](#installation)
  - [Clone api repository](#clone-api-repository)
  - [Install dependencies](#install-dependencies)
  - [Start server](#start-server)
- [Usage](#usage)
  - [Get game info](#get-game-info)
  - [Python example:](#python-example)
  - [Sample response](#sample-response)
- [Hosted Endpoint](#hosted-endpoint)

# Installation

## Clone project repository

```bash
git clone https://github.com/millionhz/LUMS-CS334-PROJECT.git
```

## Navigate to api folder

```bash
cd metacritic_api
```

## Clone api repository

```bash
git clone https://github.com/millionhz/metacritic_api.git
```

## Install dependencies

```bash
sudo apt install php-common libapache2-mod-php php-cli php-curl
```

## Start server

```bash
php -S localhost:3000
```

API will be accessible at http://localhost:3000/

# Usage

## Get game info

Send GET request with the following parameters:
- `game_title`
- `platform`

http://localhost:3000/?game_title=The%20Elder%20Scrolls%20V:%20Skyrim&platform=pc

## Python example:

```python
import requests
response = requests.get('http://localhost:3000/', params={'game_title': 'The Elder Scrolls V: Skyrim', 'platform': 'pc'})
```

## Sample response

```json
{
  "name": "The Elder Scrolls V: Skyrim",
  "metascritic_score": 94,
  "users_score": 8.2,
  "rating": "M",
  "genres": [
    "Role-Playing",
    "First-Person",
    "First-Person",
    "Western-Style"
  ],
  "developers": [
    "Bethesda Game Studios"
  ],
  "publishers": "Bethesda Softworks",
  "release_date": "Nov 10, 2011",
  "also_on": [
    "PlayStation 3",
    "Xbox 360"
  ],
  "also_on_url": [
    "/game/playstation-3/the-elder-scrolls-v-skyrim",
    "/game/xbox-360/the-elder-scrolls-v-skyrim"
  ],
  "thumbnail_url": "http://static.metacritic.com/images/products/games/7/5988ee04196a686e107b46174f94a3ae-98.jpg",
  "cheat_url": "http://www.gamefaqs.com/console/pc/code/615805.html"
}
```

# Hosted Endpoint

A hosted instance of the endpoint is available [here](https://metacritic-api.azurewebsites.net/).