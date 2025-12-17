# store/models.py
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model() 

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True) # Useful for generating clean, friendly URLs

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        related_name='products', 
        on_delete=models.SET_NULL, # Products remain even if category is deleted
        null=True
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # e.g., 1000.00
    stock = models.IntegerField(default=0)
    # Note: Requires 'Pillow' library for image handling (pip install pillow)
    image = models.ImageField(upload_to='products/', blank=True, null=True) 
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(
        User, 
    related_name='orders', 
    on_delete=models.SET_NULL, 
    null=True 
    ) 
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    STATUS_CHOICES = [
        ('P', 'Pending'), ('S', 'Shipped'), 
        ('D', 'Delivered'), ('C', 'Cancelled')
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f"Order {self.id} | User: {self.user.username if self.user else 'Guest'}"

class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    
    product = models.ForeignKey(Product, on_delete=models.PROTECT) 
    
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    quantity = models.PositiveIntegerField(default=1)
    
    def get_cost(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart for {self.user.username if self.user else 'Guest'}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product') 

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

