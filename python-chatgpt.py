import os
import requests

from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

print(api_key)