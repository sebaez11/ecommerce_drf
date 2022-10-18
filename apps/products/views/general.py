# Local imports
from apps.products.serializers.general import (MeasureUnitSerializer, 
                                               IndicatorSerializer, 
                                               CategorySerializer)
from apps.base.views import GeneralListAPIView


class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer


class CategoryListAPIView(GeneralListAPIView):
    serializer_class = CategorySerializer

