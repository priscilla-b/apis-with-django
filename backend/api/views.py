from django.http import JsonResponse
import json

# Create your views here.

def api_home(request, *args, **kwargs):
    # print(dir(request))
    print(request.GET)  # shows the url query params

    body = request.body  # byte string of JSON data

    try:
        data = json.loads(body)
    except:
        data = {}
    
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    # headers are not json serializable by default so need to be converted to dict firs
    data['content_type'] = request.content_type

   
    return JsonResponse(data)
