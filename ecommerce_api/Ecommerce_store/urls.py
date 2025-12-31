from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views 

# 1. Register your ViewSets with a Router
router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'cart', views.CartViewSet, basename='cart')
router.register(r'orders', views.OrderViewSet, basename='order')

urlpatterns = [
    path('', views.index, name='index'), # Your existing index
    
    # 2. Include the router URLs (this creates /products/, /cart/, etc.)
    path('api/v1/', include(router.urls)),
    
    # 3. Add the Token endpoints for Postman login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]