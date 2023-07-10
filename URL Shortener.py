# pip install pyshorteners

import pyshorteners

url = input("Enter url : ")

shortener = pyshorteners.Shortener()
shortenedURL = shortener.tinyurl.short(url)
print(shortenedURL)