# Using localhost as endpoint

import requests

endpoint = "http://localhost:8000"

get_response = requests.get(endpoint)  # regular http request
print(get_response.text)  # regular http response