# Third party imports
from rest_framework import generics


class GeneralListAPIView(generics.ListAPIView):
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)