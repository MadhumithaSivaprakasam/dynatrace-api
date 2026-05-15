import requests

API_TOKEN = "YOUR_API_TOKEN_HERE"
url = "https://kbn60044.live.dynatrace.com/api/v2/problems"

headers = {
    "Authorization": f"Api-Token {API_TOKEN}"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

data = response.json()

problems = data.get("problems", [])

print("\nDynatrace Problems\n")

if not problems:
    print("No active problems found.")

for problem in problems:
    print("Problem ID :", problem.get("problemId"))
    print("Title      :", problem.get("title"))
    print("Severity   :", problem.get("severityLevel"))
    print("--------------------------")