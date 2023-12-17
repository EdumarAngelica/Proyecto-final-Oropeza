from django.contrib import admin
from AppCoder.models import Product, Client, PurchaseOrder

# Register your models here.
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(PurchaseOrder)

