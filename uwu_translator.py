import os
import requests

text = input("Text to Translate: ")

text = text.lower()
text = text.replace("l", "w")
text = text.replace("r", "w")

text = text.replace("uwu", "euuw woo")
text = text.replace("owo", "oh woaw")

print(text)

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
