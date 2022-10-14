# Django
from django.contrib import admin

# Models
from .models import MeasureUnit, Category, Indicator, Product

admin.site.register(MeasureUnit)
admin.site.register(Category)
admin.site.register(Indicator)
admin.site.register(Product)