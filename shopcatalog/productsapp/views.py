from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Products


class ProductsListView(ListView):
    model = Products
    template_name = 'productsapp/products_list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('category').all()
        if 'pk' in self.kwargs:
            queryset = Products.objects.filter(category__id=self.kwargs['pk']).prefetch_related('category').all()
        return queryset


class ProductsCrateView(CreateView):
    model = Products
    fields = ['name', 'price', 'unit', 'supplier_name', 'category']
    template_name = 'productsapp/products_create.html'

    def get_success_url(self):
        return reverse_lazy('products:main')


