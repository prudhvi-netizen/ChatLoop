import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

def ask_order(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if your key supports it
        messages=messages
    )
    return response['choices'][0]['message']['content']
