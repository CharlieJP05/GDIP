import os
import ssl
import wifi
import socketpool
import adafruit_requests

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent"

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())


def call(prompt):
    headers = {"x-goog-api-key": os.getenv("GEMINI_API_KEY")}
    body = {"contents": [{"parts": [{"text": prompt}]}]}

    reply = requests.post(URL, headers=headers, json=body)
    data = reply.json()
    reply.close()

    return data["candidates"][0]["content"]["parts"][0]["text"]