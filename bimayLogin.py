import json
import requests
import os
import dotenv

dotenv.load_dotenv()
passwords = os.getenv('PASSWORD')

session = requests.session()
session.post("https://myclass.apps.binus.ac.id/Auth/Login", json={
    'Username': 'fajar.hamka',
    'Password': passwords
})

res = session.get("https://myclass.apps.binus.ac.id/Home/GetViconSchedule")
rawData = res.text
jsonData = json.loads(rawData)
print(json.dumps(jsonData, indent=4))