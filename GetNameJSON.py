import json
import requests

response = requests.get('https://zenquotes.io/api/random')
json_data = json.loads(response.text)
print(json.dumps(json_data, indent=4))
