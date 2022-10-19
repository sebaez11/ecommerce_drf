# Third-party imports
from rest_framework import serializers

# Local imports
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state', 'created_at', 'modified_at', 'deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'image': instance.image if instance.image else '',
            'measure_unit': instance.measure_unit.description,
            'category': instance.category.description,
        }