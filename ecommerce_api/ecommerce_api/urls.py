
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
    path('', include('Ecommerce_store.urls')),
] 
