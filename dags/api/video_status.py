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

def get_video_ids(playlist_id):
    video_ids = []
    pageToken = None

    try:
        while True:
            url = URL
            if pageToken:
                url += f"pageToken={pageToken}"

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            video_ids += [item["contentDetails"]["videoId"] for item in data.get("items",[])]
            pageToken = data.get("nextPageToken")
            if not pageToken:
                break
        
        return video_ids

    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    playlist_id = get_playlist_id()
    get_video_ids(playlist_id)
