import json
# from django.http import JsonResponse, HttpResponse
# from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    data = request.data  #api version of request.POST since we'll be sending in JSON data
    serializer = ProductSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        data = serializer.data
        print(data)
        return Response(data)
    else:
        return Response({'not valid': 'serializer is not valid'},status=400)


# using model data with django rest framework serializers - get request
# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API view
#     """
#     instance = Product.objects.all().order_by('?').first()  # return random model object
#     data = {}

#     if instance:
#         data = ProductSerializer(instance).data

#     return Response(data)



# using model data with manual serialization
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by('?').first()  # return random model object

#     data = {}
#     if model_data:
#         # manual serialization: model instance -> python dict -> json
#         data['id'] = model_data.id
#         data['title'] = model_data.title
#         data['content'] = model_data.content
#         data['price'] = model_data.price

#         # using model_to_dict
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])

#         # return an HttpResponse instead
#     #     json_data_string = json.dumps(data)

#     # return HttpResponse(json_data_string, headers={'content-type':'application/json'})  
#     # default content type for an HttpResponse is text/html
#     # will need to serialize fields one by one
    
#     return JsonResponse(data)



# using json data
# def api_home(request, *args, **kwargs):
#     # print(dir(request))
#     print(request.GET)  # shows the url query params

#     body = request.body  # byte string of JSON data

#     try:
#         data = json.loads(body)
#     except:
#         data = {}
    
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     # headers are not json serializable by default so need to be converted to dict firs
#     data['content_type'] = request.content_type

   
#     return JsonResponse(data)


