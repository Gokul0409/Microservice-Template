import requests

url = "http://0.0.0.0:4444/user"

data = {"sn": 1, "name": "Gokul"}

response = requests.get(url)

print(response.json())


