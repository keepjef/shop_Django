from django.contrib import admin
from django.urls import path
from .views import ProductListView, CartListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view()),
    path('cart', CartListView.as_view())
]