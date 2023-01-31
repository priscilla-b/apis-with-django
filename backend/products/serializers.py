from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    #   rename get_discount as my_discount in serializer
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_my_discount(self, obj):
        # obj is an instance of the attached model
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()