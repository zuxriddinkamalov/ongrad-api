from django.db.models import F

from rest_framework import viewsets

from apps.apartment.filters.apartment import ApartmentFilters
from apps.apartment.models import Apartment
from apps.apartment.serializer.apartment import \
    ApartmentModelSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentModelSerializer
    filter_class = ApartmentFilters

    def get_queryset(self):
        query_set = super().get_queryset()
        not_first_last = self.request.GET.get('not_first_last')
        if not_first_last:
            return query_set.exclude(floor=1).exclude(floor=F('max_floor'))
        return query_set
