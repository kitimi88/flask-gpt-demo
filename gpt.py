import os
import sys
import time
import openai
from collections import deque

openai.api_key = os.getenv("OPENAI_API_KEY")

systemPrompt = "You are a helpful assistant."

data = deque(maxlen=10) # Adjust the maximum length as per requirements

GPT_MODEL = "gpt-3.5-turbo-16k"  # Adjust accordingly.

def get_response(prompt_msg):
    if prompt_msg == "clear":
        data.clear()
        data.append({"role": "assistant", "content": 'hello'})
    else:
        data.append({"role": "assistant", "content": prompt_msg})

    messages = [{"role": "system", "content": systemPrompt}]
    messages.extend(data)
    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=messages,
            max_tokens=200,
            n=1,
            temperature=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )
        content = response["choices"][0]["message"]["content"]
        return content
    except openai.error.RateLimitError as e:
        print(e)
        return ""
