import requests
import json

# import os
# from dotenv import load_dotenv
# load_dotenv(dotenv_path="./.env")

from airflow.decorators import task
from airflow.models.variable import Variable

API_KEY = Variable.get('API_KEY')
CHANNEL_HANDLE = Variable.get('CHANNEL_HANDLE')
maxResults = 50

URL = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

@task
def get_playlist_id():
    try:
    
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        channel_items = data['items'][0]
        return channel_items['contentDetails']['relatedPlaylists']['uploads']
    
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    print(get_playlist_id())
