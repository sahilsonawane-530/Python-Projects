# pip install requests

import requests
import json
from datetime import date

date = date.today()
query = input("News you are interested in : ")
apiKey = open("C:/API/News.txt", "r").read()
url = f"https://newsapi.org/v2/everything?q={query}&from{date}&sortBy=publishedAt&apiKey={apiKey}"
r=requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")