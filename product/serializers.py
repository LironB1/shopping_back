from rest_framework import serializers
from .models import Product
from .models import CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True) #nested serializer

    class Meta:
        model = CartItem
        fields = '__all__'