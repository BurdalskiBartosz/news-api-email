import requests
from dotenv import load_dotenv
import os

from send_email import send_email

load_dotenv()

api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-01-02&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()

message = ""
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2* "\n"

body = body.encode('utf-8')
send_email(body)