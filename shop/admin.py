from django.contrib import admin
from .models import Category, Product, Cart

myModels = [Category, Product, Cart]
admin.site.register(myModels)
