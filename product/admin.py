from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['payment_status','status']