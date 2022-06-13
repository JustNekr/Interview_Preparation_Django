from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy


class Supplier(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = Manager()
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.name


class Products(models.Model):
    class Meta:
        ordering = ['name']

    class Unit(models.TextChoices):
        PIECES = 'PC', gettext_lazy('Штук')
        KILOGRAM = 'KG', gettext_lazy('Килограм')

    name = models.CharField(max_length=64)
    entrance_data = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    unit = models.CharField(max_length=2, choices=Unit.choices, default=Unit.PIECES)
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ManyToManyField(ProductCategory, verbose_name='Категория')
    site = models.ManyToManyField(Site)
    objects = Manager()
    on_site = CurrentSiteManager('site')
    # image = models.ImageField(verbose_name='Фото')


