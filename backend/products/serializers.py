from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    #   rename get_discount as my_discount in serializer

    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', 
        lookup_field='pk'
        )
    # email = serializers.EmailField(write_only=True)

    title = serializers.CharField(validators=[
        validators.validate_title_no_hello, 
        validators.unique_product_title
        ])
    
    name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Product
        fields = [
            'url',
            # 'email',
            'pk',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f'{value} is already a product name' )
        return value

    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     # get the request object if exists in serializer 
    #     # depends on the context in which serializer is used
    #     if request is None:
    #         return None
    #     else:
    #         reverse('product-detail',kwargs={'pk':obj.pk}, request=request)

    def get_my_discount(self, obj):
        # obj is an instance of the attached model
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()