# You can find this code for Chainlit python streaming here (https://docs.chainlit.io/concepts/streaming/python)

# OpenAI Chat completion

import openai #importing openai for API usage
import chainlit as cl #importing chainlit for our app

# You only need the api key inserted here if it's not in your .env file
#openai.api_key = "YOUR_API_KEY"

# We select our model. If you do not have access to GPT-4, please use GPT-3.5T (gpt-3.5-turbo)

model_name = "gpt-3.5-turbo"
# model_name = "gpt-4"
settings = {
    "temperature": 0.7, # higher value increases output diveresity/randomness
    "max_tokens": 500, # maximum length of output response
    "top_p": 1, # choose only the top x% of possible words to return
    "frequency_penalty": 0, # higher value will result in the model being more conservative in its use of repeated tokens.
    "presence_penalty": 0, # higher value will result in the model being more likely to generate tokens that have not yet been included in the generated text
}

@cl.on_chat_start # marks a function that will be executed at the start of a user session
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )


@cl.on_message # marks a function that should be run each time the chatbot receives a message from a user
async def main(message: str):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message})

    msg = cl.Message(content="")

    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()
