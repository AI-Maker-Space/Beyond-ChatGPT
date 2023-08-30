# Beyond-ChatGPT
Chainlit App using Python streaming for Level 0 MLOps

LLM Application with Chainlit, Docker, and Huggingface Spaces
In this guide, we'll walk you through the steps to create a Language Learning Model (LLM) application using Chainlit, then containerize it using Docker, and finally deploy it on Huggingface Spaces.

Prerequisites
A GitHub account
Docker installed on your local machine
A Huggingface Spaces account


### Building our App
Clone [this](https://github.com/AI-Maker-Space/Beyond-ChatGPT/tree/main) repo.

``` bash
git clone https://github.com/AI-Maker-Space/Beyond-ChatGPT.git
```

Navigate inside this repo
```
cd Beyond-ChatGPT
```

Install the packages required for this python envirnoment in `requirements.txt`.
```
pip install -r requirements.txt
```

Open your `.env` file. Replace the `###` in your `.env` file with your OpenAI Key and save the file.
```
OPENAI_API_KEY=sk-###
```

Let's try deploying it locally. Make sure you're in the python environment where you installed Chainlit and OpenAI.

Run the app using Chainlit

```
chainlit run app.py -w
```

Great work! Let's see if we can interact with our chatbot.

Time to throw it into a docker container a prepare it for shipping

Build the Docker image. We'll tag our image as `llm-app` using the `-t` parameter. The `.` at the end means we want all of the files in our current directory to be added to our image.
``` bash
docker build -t llm-app .
```

Run and test the Docker image locally using the `run` command. The `-p`parameter connects our **host port #** to the left of the `:` to our **container port #** on the right.
``` bash
docker run -p 7860:7860 llm-app
```

Visit http://localhost:7860 in your browser to see if the app runs correctly.

Great! Time to ship!

### Deploy to Huggingface Spaces

Make sure you're logged into Huggingface Spaces CLI

``` bash
huggingface-cli login
```

Follow the prompts to authenticate.


Deploy to Huggingface Spaces


Create a new Huggingface Space

- Owner: Your username
- Space Name: `llm-app`
- License: `Openrail`
- Select the Space SDK: `Docker`
- Docker Template: `Blank`
- Space Hardware: `CPU basic - 2 vCPU - 16 GB - Free`
- Repo type: `Public`



Deploying on Huggingface Spaces using a custom Docker image involves using their web interface. Go to Huggingface Spaces and create a new space, then set it up to use your Docker image from the Huggingface Container Registry.

Access the Application

Once deployed, access your app at:

ruby
Copy code
https://huggingface.co/spaces/your-username/llm-app
Conclusion
You've successfully created an LLM application with Chainlit, containerized it with Docker, and deployed it on Huggingface Spaces. Visit the link to interact with your deployed application.
