import requests
from secrets import groq_key

URL = "https://api.groq.com/openai/v1/chat/completions"

def call(prompt, model="openai/gpt-oss-120b"):
    reply = requests.post(
        URL,
        headers={"Authorization": "Bearer " + groq_key},
        json={"model": model,
            "reasoning_effort": "low",
            "response_format": {"type": "json_object"},
            "temperature": 0.6,
            "top_p": 0.95,
            "max_completion_tokens": 1024,
            "include_reasoning": False,
            "messages": [{"role": "user", "content": prompt}]},)
    data = reply.json()
    reply.close()

    return data["choices"][0]["message"]["content"]