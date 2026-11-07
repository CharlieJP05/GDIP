import requests
from secrets import groq_key

URL = "https://api.groq.com/openai/v1/chat/completions"

def call(prompt, model="openai/gpt-oss-120b"):
    reply = requests.post(
        URL,
        headers={"Authorization": "Bearer " + groq_key},
        json={"model": model,
            "messages": [{"role": "user", "content": prompt}]})
    data = reply.json()
    reply.close()

    return data["choices"][0]["message"]["content"]