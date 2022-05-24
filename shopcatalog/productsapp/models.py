from django.db import models
from django.utils.translation import gettext_lazy


class Supplier(models.Model):
    name = models.CharField(max_length=64)


class Products(models.Model):
    class Unit(models.TextChoices):
        PIECES = 'PC', gettext_lazy('Штук')
        KILOGRAM = 'KG', gettext_lazy('Килограм')

    name = models.CharField(max_length=64)
    entrance_data = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    unit = models.CharField(max_length=2, choices=Unit.choices, default=Unit.PIECES)
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE)



