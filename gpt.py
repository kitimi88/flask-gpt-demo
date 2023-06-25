import os
import sys
import time
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

systemPrompt = { "role": "system", "content": "You are a helpful assistant." }
data = []

MODEL = "gpt-3.5-turbo-16k" # adjust accordingly.

def get_response(promt_msg):
    if promt_msg == "clear":
        #data.clear()
        data.append({"role": "assistant", "content": 'hello'})
    else:  
        data.append({"role": "assistant", "content": promt_msg})

    messages = [ systemPrompt ]
    messages.extend(data)
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
            max_tokens=256,
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