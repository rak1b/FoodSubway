from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategoryChoices(models.IntegerChoices):
    FRUITS = 0, _("Fruits")
    VEGETABLE = 1, _("Vegetable")
    FISH = 2, _("Fish")
    DRY_FRUITS = 3, _("Dry Fruits")
    EGG = 4, _("Egg")
    CHICKEn = 5, _("Chicken")
    OTHER = 6, _("Other")

class OrderStatusChoices(models.IntegerChoices):
    ACTIVE = 0, _("On The Way")
    DELIVERED = 1, _("Delivered")
    CANCELLED = 2, _("Cancelled")

class PaymentStatusChoices(models.IntegerChoices):
    PAID = 0, _("Paid")
    UNPAID = 1, _("Unpaid")
    DUE = 2, _("Due")