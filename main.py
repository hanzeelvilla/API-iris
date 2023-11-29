import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    "features": [[5.4,2.6,4.1,1.3]]
}

response = requests.post(url, json=data)

print(response.json())
