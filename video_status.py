import requests
import json

API_KEY = ""
CHANNEL_HANDLE = "MrBeast"

URL = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"


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
