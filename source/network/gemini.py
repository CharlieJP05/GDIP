import requests
from secrets import api_key

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent"

def call(prompt):
    headers = {"x-goog-api-key": api_key}
    body = {"contents": [{"parts": [{"text": prompt}]}]}

    reply = requests.post(URL, headers=headers, json=body)
    data = reply.json()
    reply.close()

    return data["candidates"][0]["content"]["parts"][0]["text"]