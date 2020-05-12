import os
import requests

text = input("Text to Translate: ")

text = text.lower()
text = text.replace("l", "w")

info = {
    "text": f"{text}",
    "character": "Fluttershy",
    "emotion": "Neutral"
}

url = "https://api.fifteen.ai/app/getAudioFile"

response = requests.post(url, data=info, timeout=120.0)

print(response.status_code)

f = open("uwu.wav", 'wb')
f.write(response.content)
f.close()
