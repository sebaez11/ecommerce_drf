# Standard imports
from django.urls import path

# Local imports
from apps.products.views.general import (MeasureUnitListAPIView,
                                         IndicatorListAPIView,
                                         CategoryListAPIView)


urlpatterns = [
    path(
        route='measure-unit/',
        view=MeasureUnitListAPIView.as_view(),
        name='measure-unit'
    ),
    path(
        route='indicator/',
        view=IndicatorListAPIView.as_view(),
        name='indicator'
    ),
    path(
        route='category/',
        view=CategoryListAPIView.as_view(),
        name='category'
    ),
]
