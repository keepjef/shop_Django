from django.contrib import admin
from .models import Category, Product, ProductInOrder, Order

myModels = [Category, Product, ProductInOrder, Order]
admin.site.register(myModels)
