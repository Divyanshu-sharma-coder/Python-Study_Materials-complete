# Write a progrm to pronouce list of name using win32 API

import os
import time
from gtts import gTTS
import pygame as pg

pg.mixer.init()

li = ["Divyanshu", "Alex", "Drake", "Kendrik"]

for name in li:
    text_say = f"Shoutout to {name}"

    tts = gTTS(text= text_say, lang='en', tld = 'com')
    audio = "shoutout.mp3"
    tts.save(audio)

    pg.mixer.music.load(audio)
    pg.mixer.music.play()

    while pg.mixer.music.get_busy():
        time.sleep(0.1)

    pg.mixer.music.unload()
    os.remove(audio)


