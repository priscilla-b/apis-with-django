# Using localhost as endpoint

import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(
    endpoint,
    params={"abc":123},
    json={"query":"hello world"}
    )  # regular http request

# print(get_response.url)
print(get_response.json())  # regular http response