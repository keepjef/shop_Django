from django.shortcuts import render
from .models import Product
from django.views.generic import ListView


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class CartListView(ListView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context