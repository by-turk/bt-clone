import requests
import json

web_url = 'http://127.0.0.1:5000/webhook'

data = {
    "test": "hhhjhkkhkj"
}

r = requests.post(web_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Print the response from the server
print(r.json())
