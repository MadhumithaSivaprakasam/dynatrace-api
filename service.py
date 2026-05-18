from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_TOKEN = os.getenv("DYNATRACE_API_TOKEN")

url = "https://kbn60044.live.dynatrace.com/api/v2/problems"

@app.route('/')
def home():
    return "Dynatrace Microservice is Running"

@app.route('/problems', methods=['GET'])
def get_problems():

    headers = {
        "Authorization": f"Api-Token {API_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)