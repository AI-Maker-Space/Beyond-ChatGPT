# You can find this code for Chainlit python streaming here (https://docs.chainlit.io/concepts/streaming/python)

# OpenAI Chat completion

import openai #importing openai for API usage
import chainlit as cl #importing chainlit for our app
from chainlit.input_widget import Select, Switch, Slider #importing chainlit settings selection tools
from chainlit.prompt import Prompt, PromptMessage #importing prompt tools 
from chainlit.playground.providers import ChatOpenAI #importing ChatOpenAI tools

# You only need the api key inserted here if it's not in your .env file
#openai.api_key = "YOUR_API_KEY"

# ChatOpenAI Templates
system_template = """You are a helpful assistant who always speaks in a pleasant tone!
"""

user_template = """{input}
Think through your response step by step.
"""

@cl.on_chat_start # marks a function that will be executed at the start of a user session
async def start_chat():
    settings = {
        "model": "gpt-3.5-turbo",
        "temperature": 0,
        "max_tokens": 500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    cl.user_session.set("settings", settings)

@cl.on_message # marks a function that should be run each time the chatbot receives a message from a user
async def main(message: str):

    settings = cl.user_session.get("settings")

    prompt = Prompt(
        provider=ChatOpenAI.id,
        messages=[
            PromptMessage(
                role="system",
                template=system_template,
                formatted=system_template,
            ),
            PromptMessage(
                role="user",
                template=user_template, 
                formatted=user_template.format(input=message),
            )
        ],
        inputs = {"input" : message},
        settings=settings
    )

    print([m.to_openai() for m in prompt.messages])

    msg = cl.Message(content="")

    # Call OpenAI
    async for stream_resp in await openai.ChatCompletion.acreate(
        messages=[m.to_openai() for m in prompt.messages], stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    # Update the prompt object with the completion
    prompt.completion = msg.content
    msg.prompt = prompt

    # Send and close the message stream
    await msg.send()
