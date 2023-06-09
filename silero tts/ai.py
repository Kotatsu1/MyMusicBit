import openai

def chat(message):

    message_log = [
    {"role": "system", "content": "Ты женщина, голосовой ассистент Лит, тебя разработал Котатсу."}
    ]


    openai.api_key = "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"
    messages = message_log
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=256)
    reply = chat.choices[0].message.content

    if len(reply) > 999:
        reply = reply[0:999]
        return reply
    return reply
