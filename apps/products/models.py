# Django imports
from django.db import models

# Local imports
from apps.base.models import BaseModel


class MeasureUnit(BaseModel):
    description = models.CharField(max_length=50, 
                                   blank=False, null=False, 
                                   unique=True)
    
    class Meta:
        verbose_name = 'Measure Unit'

    def __str__(self):
        return self.description
    

class Category(BaseModel):
    description = models.CharField(max_length=50, 
                                   unique=True, null=False, 
                                   blank=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.description


class Indicator(BaseModel):
    discount = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Indicator"

    def __str__(self):
        return f'{self.category}:{self.discount}%'


class Product(BaseModel):
    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null = False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name = 'Product'

    def __str__(self):
        return self.name