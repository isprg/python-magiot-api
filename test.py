import requests
import json
import sys

url = "http://localhost:1323/api/v1/devices"

json_data = {
    "name": sys.argv[1]
}

response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    data=json.dumps(json_data)
)

res_data = response.json()
print(response)
