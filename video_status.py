import requests
import json

API_KEY = ""
CHANNEL_HANDLE = "MrBeast"

URL = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

response = requests.get(URL)
print(json.dumps(response.json(), indent=4))