import os
import random

musicDir = input("Enter path to music directory : ")
songs = os.listdir(musicDir)
randomSong = songs[random.randint(0,5)]
os.startfile(os.path.join(musicDir, randomSong))
print("Playing...")
print(randomSong.removesuffix(".mp3" or ".mp4" or ".webm"))