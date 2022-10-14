# Third-party imports
from rest_framework import serializers

# Local imports
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state',)