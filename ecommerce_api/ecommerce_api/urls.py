"""
URL configuration for ecommerce_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Ecommerce_store import views as Ecommerce_views


router = DefaultRouter()
router.register(r'categories', Ecommerce_views.CategoryViewSet)
router.register(r'products', Ecommerce_views.ProductViewSet)
router.register(r'cart', Ecommerce_views.CartViewSet, basename='cart')
router.register(r'cart-items', Ecommerce_views.CartItemViewSet, basename='cart-item')
router.register(r'orders', Ecommerce_views.OrderViewSet, basename='order')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
