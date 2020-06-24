from django.contrib import admin
from .models import Category, Product

myModels = [Category, Product]
admin.site.register(myModels)
