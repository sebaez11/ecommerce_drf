# Local imports
from apps.products.serializers import ProductSerializer
from apps.base.views import GeneralListAPIView


class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer