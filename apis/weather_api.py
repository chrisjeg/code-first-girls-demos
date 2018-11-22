import requests
import json

endpoint = "http://api.openweathermap.org/data/2.5/weather"
parameters = {
    "q": "London,uk",
    "appid": "YOUR_KEY"
}

response = requests.get(endpoint, params=parameters)

print response.url
print response.status_code
print response.headers["content-type"]
print response.text

# Retrieving data from the response
print json.loads(response.text)['main']['temp']
for item in json.loads(response.text)['weather']:
    print item['main']

