import requests
from app.auth.auth import headers

URL = "https://kbn60044.live.dynatrace.com/api/v2/problems"

def get_problems():

    response = requests.get(URL, headers=headers)

    return response.json()


def get_problem_by_id(problem_id):

    url = f"https://kbn60044.live.dynatrace.com/api/v2/problems/{problem_id}"

    response = requests.get(url, headers=headers)

    return response.json()