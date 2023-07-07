# CLUTTERED FOLDER
# https://github.com/Sahil530Sonawane/Small-Python-Projects/tree/master/CTC%202

import os
import shutil

codeFiles = ".py", ".js", ".css", ".html", ".php", ".c", ".c++"
imageFiles = ".jpg", ".png", ".gif", ".psd"
excelFiles = ".xlsx", ".csv"
zipFiles = ".zip", ".rar", ".jar"
mediaFiles = ".mp3", ".mp4"

files = os.listdir("Helping/CTC 2/")
for i in files:
    print(i)
    if (i.endswith(codeFiles)):
        os.makedirs("Helping/CTC 2/Code", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Code")

    elif (i.endswith(imageFiles)):
        os.makedirs("Helping/CTC 2/Images", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Images/")

    elif (i.endswith(".pdf")):
        os.makedirs("Helping/CTC 2/Documents/pdf", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Documents/pdf")
    
    elif (i.endswith(".pptx")):
        os.makedirs("Helping/CTC 2/Documents/pptx", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Documents/pptx/")
    
    elif (i.endswith(".docx")):
        os.makedirs("Helping/CTC 2/Documents/word", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Documents/word/")
    
    elif (i.endswith(excelFiles)):
        os.makedirs("Helping/CTC 2/Documents/excel", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Documents/excel/")
    
    elif (i.endswith(mediaFiles)):
        os.makedirs("Helping/CTC 2/Media", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Media/")
    
    elif (i.endswith(".accdb")):
        os.makedirs("Helping/CTC 2/Documents/database", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Documents/database/")
    
    elif (i.endswith(".pub")):
        os.makedirs("Helping/CTC 2/Documents/publish", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Documents/publish/")
    
    elif (i.endswith(".txt")):
        os.makedirs("Helping/CTC 2/Documents/txt", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Documents/txt/")
    
    elif (i.endswith(zipFiles)):
        os.makedirs("Helping/CTC 2/Zip", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Zip/")
    
    elif (i.endswith(".exe")):
        os.makedirs("Helping/CTC 2/Exe", exist_ok=True)
        shutil.move(f"Helping/CTC 2/{i}", "Helping/CTC 2/Exe/")