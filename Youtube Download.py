# pip install pytube
# https://github.com/pytube/pytube/issues/1678#issuecomment-1605009831

import os
from pytube import YouTube

def Audio():
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first().download(filename=filename)
    print("Your file is saved at", os.path.abspath(filename))

def Video():
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution().download(filename=filename)
    print("Your file is saved at", os.path.abspath(filename))

url = input("Enter url : ")
downloadFormat = input("Enter format : ")
filename = input("Enter file name : ")

try:
    yt=YouTube(url)
    if (downloadFormat == "Video") or (downloadFormat == "video") or (downloadFormat == ".mp4") or (downloadFormat == "mp4"):
        Video()
    
    elif (downloadFormat == "Audio") or (downloadFormat == "audio") or (downloadFormat == ".mp3") or (downloadFormat == "mp3") or (downloadFormat == ".webm") or (downloadFormat == "webm"):
        Audio()
    else:
        raise ValueError()

except Exception as e:
    print(f"Error: {e}")