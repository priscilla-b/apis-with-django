import requests

product_id = input('What is the id of the product you want to delete?\n')

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not a valid id')

endpoint = "http://localhost:8000/api/products/{product_id}/delete/"
data = {
    'title':'Hello world my old friend',
    'price': 129.99
}
get_response = requests.delete(endpoint, json=data)
print(get_response.json())