from django.contrib import admin

# Register your models here.
from .models import Supplier, Products, ProductCategory

admin.site.register(Supplier)
admin.site.register(Products)
admin.site.register(ProductCategory)