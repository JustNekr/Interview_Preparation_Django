from django.contrib import admin

# Register your models here.
from .models import HitCount

admin.site.register(HitCount)
