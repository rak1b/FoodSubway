from unicodedata import category
from django.db import models
from product import constants
from core.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
# Create your models here.


class Product(BaseModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    name = models.CharField(max_length=200)
    category = models.SmallIntegerField(choices=constants.ProductCategoryChoices.choices)
    price_for_1kg = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    price_for_3kg = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    price_for_5kg = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    sold = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    
    def __str__(self):
          return self.title
          


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_status = models.SmallIntegerField(choices=constants.PaymentStatusChoices.choices, default=1)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    due = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    delivery_charge = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    status = models.SmallIntegerField(choices=constants.OrderStatusChoices.choices, default=0)

    def __str__(self):
          return self.order.title
          