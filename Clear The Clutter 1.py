# CLUTTERED FOLDER
# https://github.com/Sahil530Sonawane/Small-Python-Projects/tree/master/CTC%201

import os

files = os.listdir("Helping/CTC 1/")
fileFormat = input("Enter file format : ")
i = 1
for file in files:
    if file.endswith(f".{fileFormat}"):
        print(file)
        os.rename(f"Helping/CTC 1/{file}", f"Helping/CTC 1/{i}.{fileFormat}")
        i = i + 1