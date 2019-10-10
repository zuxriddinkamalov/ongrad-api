from rest_framework import viewsets

from apps.apartment.filters.apartment import ApartmentFilters
from apps.apartment.models import Apartment
from apps.apartment.serializer.apartment import \
    ApartmentModelSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentModelSerializer
    filter_class = ApartmentFilters
