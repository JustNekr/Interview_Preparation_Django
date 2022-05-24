from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Products


class ProductsListView(ListView):
    model = Products
    template_name = 'productsapp/products_list.html'
    context_object_name = 'products'
    paginate_by = 5


class ProductsCrateView(CreateView):
    model = Products
    fields = ['name', 'price', 'unit', 'supplier_name']
    template_name = 'productsapp/products_create.html'
