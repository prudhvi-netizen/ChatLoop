import os
import chainlit as cl
from openai import OpenAI

# Use environment variable or hardcode your key (not recommended)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@cl.on_message
async def handle_message(message: cl.Message):
    try:
        # Send user's input to OpenAI and get the response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.content}
            ]
        )

        reply = response.choices[0].message.content
        await cl.Message(content=reply).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()
