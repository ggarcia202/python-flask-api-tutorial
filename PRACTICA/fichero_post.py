import requests

url = "http://localhost/persons"

data = {
    "name": "Fiona",
    "age": 27,
    "city": "Boston",
    "occupation": "Lawyer",
    "hobbies": ["Writing", "Traveling", "Cooking"]
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response:", response.json())


