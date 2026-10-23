import requests #type: ignore

url = "https://fake-json-api.mock.beeceptor.com/users"

response = requests.get(url = url)

print(response.json())