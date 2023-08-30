# Beyond-ChatGPT
Chainlit App using Python streaming for Level 0 MLOps

LLM Application with Chainlit, Docker, and Huggingface Spaces
In this guide, we'll walk you through the steps to create a Language Learning Model (LLM) application using Chainlit, then containerize it using Docker, and finally deploy it on Huggingface Spaces.

Prerequisites
A GitHub account
Docker installed on your local machine
A Huggingface Spaces account

### Building our App
Clone this repo

Navigate inside this repo

### Install requirements using `pip install -r requirements.txt`?????????

Add your OpenAI Key to `.env` file and save the file.

Let's try deploying it locally. Make sure you're in the python environment where you installed Chainlit and OpenAI.

Run the app using Chainlit

```
chainlit run app.py -w
```

Great work! Let's see if we can interact with our chatbot.

It works! Let's ship it!


### Deploy to Huggingface Spaces

Login to Huggingface Spaces CLI

``` bash
huggingface-cli login
```

Follow the prompts to authenticate.



Push Docker Image to Huggingface Container Registry

```
docker tag llm-app:latest huggingface/your-username/llm-app:latest
docker push huggingface/your-username/llm-app:latest
```

Deploy to Huggingface Spaces


Deploying on Huggingface Spaces using a custom Docker image involves using their web interface. Go to Huggingface Spaces and create a new space, then set it up to use your Docker image from the Huggingface Container Registry.

Access the Application

Once deployed, access your app at:

ruby
Copy code
https://huggingface.co/spaces/your-username/llm-app
Conclusion
You've successfully created an LLM application with Chainlit, containerized it with Docker, and deployed it on Huggingface Spaces. Visit the link to interact with your deployed application.
