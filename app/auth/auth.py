import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("DYNATRACE_API_TOKEN")

headers = {
    "Authorization": f"Api-Token {API_TOKEN}"
}