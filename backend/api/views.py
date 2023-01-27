from django.http import JsonResponse
import json

# Create your views here.

def api_home(request, *args, **kwargs):
    # print(dir(request))
    body = request.body  # byte string of JSON data
    print('body',body)

    # data = json.loads(body)
    # print('data', data)
    
    # try:
    #     data = json.loads(body)
    # except:
    #     data = {}
    #     print('empty data')
    #     print(Exception)
    return JsonResponse({"message":"Hi there, this is your Django API resonse!"})
