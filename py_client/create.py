import requests


headers = {'Authorization': 'Bearer 2ce728093978ca34c3680be2f0cc0844a8ad6be3'}

endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'Create with token',
    'price': 32.99
}
# get_response = requests.get(endpoint)
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())