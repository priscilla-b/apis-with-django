import requests

# *** Using an example endpoint ***
endpoint = "https://httpbin.org/anything"
# like your url. going to be many endpoints in an api project

get_response = requests.get(endpoint)  # http request
print(get_response.text)  # raw text response(response body)

# can send a json object or raw data(form) within a request
get_response_json = requests.get(endpoint, json={"query":"hello world"})
# print(get_response_json.json())

get_response_form = requests.get(endpoint, data={"query":"hello world"})
# print(get_response_form.json())

# response status code
print(get_response.status_code)