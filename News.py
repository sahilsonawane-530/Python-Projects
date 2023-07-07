# pip install requests

import requests
import json
from datetime import date

date = date.today()
query = input("News you are interested in : ")
url = f"https://newsapi.org/v2/everything?q={query}&from{date}&sortBy=publishedAt&apiKey=62654f70fea24d519fdf5a3e0a81b677"
r=requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")