from rest_framework import generics, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from django.http import Http404

from api.authentication import TokenAuthentication
# from api.permissions import IsStaffEditorPermission
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

from .models import Product
from .serializers import ProductSerializer




class ProductListCreateApiView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.ListCreateAPIView,
    ):
    # can combine list and create views if using the same endpoint
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    # allow_staff_view = False

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self):

    #     qs = super().get_queryset()
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return qs.filter(user = user)
    #     else:
    #         return Product.objects.none


   
class ProductDetailApiView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsStaffEditorPermission]
    # lookup_field = 'pk'

class ProductUpdateApiView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [IsStaffEditorPermission]
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()


class ProductDestroyApiView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [IsStaffEditorPermission]
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


# combining all views into one function
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == 'GET':

#         if pk is not None:
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             # detail view
#             return Response(data)
#         else:
#             queryset = Product.objects.all()
#             data = ProductSerializer(queryset, many=True).data
#             return Response(data)

#     if method == 'POST':
#         # create an item
#         data = request.data  #api version of request.POST since we'll be sending in JSON data
#         serializer = ProductSerializer(data=data)

#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validate_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
        
#         return Response({'not valid': 'serializer is not valid'},status=400)

