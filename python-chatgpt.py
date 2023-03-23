import os
import requests

from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

# I am using the completions API
url = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(api_key)
    }

data = {
    "model": "text-davinci-003",
    "prompt":"Write a pytest test for post request for fastAPI", # You can change test in prompt to any thing you wish to ask GPT
    "max_tokens": 2000,
    "temperature": 0.3
}

# Send a POST request to the API with the data included
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.json()["choices"][0]["text"])