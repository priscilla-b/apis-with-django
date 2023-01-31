import requests

endpoint = "http://localhost:8000/api/products/3/update/"
data = {
    'title':'please update content',
    'price': 30.00
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())