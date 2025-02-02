import requests
from dotenv import load_dotenv
import os

from send_email import send_email

load_dotenv()
topic = "tesla"

api_key = os.getenv("API_KEY")
url = ("https://newsapi.org/v2/everything"
       f"?q={topic}&from=2025-01-02&sortBy=publishedAt&apiKey={api_key}&language=en")

request = requests.get(url)
content = request.json()

message = ""
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = (body + article["title"] + "\n"
               + article["description"]
               + "\n" + article["url"] + 2*"\n")

body = "Subject: Today's news" + "\n" + body
send_email(body.encode('utf-8'))