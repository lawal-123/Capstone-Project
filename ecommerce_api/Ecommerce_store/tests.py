from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Product, Cart, CartItem, Order, OrderItem
User = get_user_model()
# Create your tests here.

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Laptop',
            price=999.99,
            stock=10,
            available=True
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Laptop')
        self.assertEqual(self.product.stock, 10)
        self.assertTrue(self.product.available)
        self.assertEqual(self.product.category.name, 'Electronics')

    def test_product_str_representation(self):
        self.assertEqual(str(self.product), 'Test Laptop')
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }

class ECommerceAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apiuser', password='securepassword')
        self.tokens = get_tokens_for_user(self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.tokens["access"]}')
        self.category = Category.objects.create(name='Books', slug='books')
        self.product1 = Product.objects.create(category=self.category, name='Book A', price=20.00, stock=5)
        self.product2 = Product.objects.create(category=self.category, name='Book B', price=10.00, stock=3)

    def test_order_placement_from_cart(self):
        cart_add_url = reverse('cart-item-list') 
        response = self.client.post(cart_add_url, {'product': self.product1.id, 'quantity': 2}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cart_retrieve_url = reverse('cart-list') 
        response = self.client.get(cart_retrieve_url)
        self.assertTrue(response.data['items']) 
        order_place_url = reverse('order-place-order') 
        response = self.client.post(order_place_url, {}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.tokens["access"]}')
        response = self.client.post(cart_add_url, {'product': self.product1.id, 'quantity': 2})
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, f"Failed to place order: {response.data}")
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 0)
        order = Order.objects.get(id=response.data['id'])
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.total_amount, 40.00) 
        self.assertEqual(order.items.count(), 1)
        self.product1.refresh_from_db() 
        self.assertEqual(self.product1.stock, 3) 
        order_item = order.items.first()
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.price, 20.00)

    def test_place_order_empty_cart(self):
        order_place_url = reverse('order-place-order')
        response = self.client.post(order_place_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('empty', response.data['detail'])