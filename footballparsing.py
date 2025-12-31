import pandas as pd
import requests

url = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json"
competitions = requests.get(url).json()

for comp in competitions:
    print(comp["competition_name"], comp["season_name"], comp["season_id"])

competition_id = 43
season_id = 3

matches_url = f"https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/{competition_id}/{season_id}.json"
matches = requests.get(matches_url).json()

for match in matches:
    print(match['home_team']['home_team_name'], match['away_team']['away_team_name'])
