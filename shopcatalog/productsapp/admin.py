from django.contrib import admin

# Register your models here.
from .models import Supplier, Products

admin.site.register(Supplier)
admin.site.register(Products)
