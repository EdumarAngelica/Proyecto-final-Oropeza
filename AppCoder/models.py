from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    characteristics = models.CharField(max_length=100)
    sku = models.CharField(max_length=255, blank=True, null=True)
    locked_stock = models.PositiveBigIntegerField()
    available_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Product {self.title}"


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rut = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    client_name = models.CharField(max_length=50)
    client_rut = models.CharField(max_length=11)
    order_number = models.PositiveBigIntegerField(unique=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.client_name