import requests

API_KEY = ""
CHANNEL_HANDLE = "MrBeast"

URL = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forhHandle={CHANNEL_HANDLE}&key={API_KEY}"

response = requests.get(URL)
print(response)