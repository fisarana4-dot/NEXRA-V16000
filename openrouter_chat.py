
import requests

API_KEY = "your_openrouter_api_key_here"
URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_model(prompt, model="z-ai/glm-5.3-flash:free"):
    headers = {
