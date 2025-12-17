from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, Cart, CartItem
from django.contrib.auth import get_user_model

User = get_user_model()
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 
            'stock', 'image', 'available', 'category', 'category_name'
        )

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'product_name', 'quantity')
        read_only_fields = ('cart',) # Cart is set by the view, not the user

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_at', 'items', 'total_items')
        read_only_fields = ('user',)

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())



class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_name', 'price', 'quantity', 'get_cost')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'user', 'user_email', 'created_at', 'status', 'total_amount', 'items')
        read_only_fields = ('user', 'total_amount', 'status')