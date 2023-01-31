# Using localhost as endpoint

import requests

# endpoint = "http://localhost:8000/api/"

# get_response = requests.post(
#     endpoint,
#     params={"abc":123},
#     json={"content":"hello world"}
#     )  # regular http request

endpoint = "http://localhost:8000/api/products/200"
get_response = requests.get(endpoint)
# print(get_response.url)
print(get_response.json())  # regular http response