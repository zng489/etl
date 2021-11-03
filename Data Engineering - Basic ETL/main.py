import sqlalchemy
from sqlalchemy.orm import sessionmaker



import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime
import datetime


#DATABASE_LOCATION = 
#USER_ID = ""
TOKEN = "BQA9mOjzOUv4NmWAqS-mHF8vjJD7EbPGYiiBQvFUw-5x63UddTVvgeBBLpjd_cDPriXrs0znK4OrbAE-FjfFTXAeackLv5EYnoIlRpM-OdUKJkFASt3zPxitZjvqvarUp6sKzuJ_N5a_EHvbwrztvkrZFwLeT8ZXptxt"


if __name__ == "__main__":
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN) 
    }

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

data = r.json()

print(data)

data_1 = []
data_2 = []

for each_data in data:
    