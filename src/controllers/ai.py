import openai
from dotenv import load_dotenv
import os

load_dotenv()

def chat(message):

    message_log = [
    {"role": "system", "content": "Ты женщина, голосовой ассистент Лит, тебя разработал Котатсу."}
    ]


    openai.api_key = os.getenv("OPENAI_API")
    messages = message_log
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=256)
    reply = chat.choices[0].message.content

    if len(reply) > 999:
        reply = reply[0:999]
        return reply
    return reply
