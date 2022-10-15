# Third-party imports
from rest_framework import generics

# Local imports
from apps.products.models import MeasureUnit, Indicator, Category
from apps.products.serializers.general import (MeasureUnitSerializer, 
                                               IndicatorSerializer, 
                                               CategorySerializer)


class MeasureUnitListAPIView(generics.ListAPIView):
    queryset = MeasureUnit.objects.filter(state=True)
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(generics.ListAPIView):
    queryset = Indicator.objects.filter(state=True)
    serializer_class = IndicatorSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(state=True)
    serializer_class = CategorySerializer

