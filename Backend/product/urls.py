from django.urls import path
from .views import  ProductList,OrderView
urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:id>', ProductList.as_view(), name='products retrieve'),
    path('orders/', OrderView.as_view(), name='orders'),

]