import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-01-02&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()

for item in content["articles"]:
    print(item['title'])