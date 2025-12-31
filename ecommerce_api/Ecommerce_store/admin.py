from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order  # Import your models here

# Register your models so they show up in the screenshot you sent
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Category)
# Register your models here.
