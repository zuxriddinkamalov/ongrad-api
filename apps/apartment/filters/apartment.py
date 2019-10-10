from django.db.models import F
import django_filters as filters
from django_filters.filters import Filter
from rest_framework.exceptions import ValidationError

from ..models import Apartment


class ListFilter(Filter):
    def filter(self, queryset, value):
        if not value:
            return queryset
        list_values = value.split(',')
        if not all(item.isdigit() for item in list_values):
            raise ValidationError(
                'All values in %s the are not integer' % str(list_values))
        return super().filter(queryset, list_values)


class ApartmentFilters(filters.FilterSet):
    year = filters.DateFromToRangeFilter()
    rooms = ListFilter(field_name='rooms', lookup_expr='in')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    not_first_last = filters.BooleanFilter(method='filter_by_floor')
    start_floor = filters.NumberFilter(field_name="max_floor",
                                       lookup_expr='gte')
    last_floor = filters.NumberFilter(field_name="max_floor",
                                      lookup_expr='lte')

    def filter_by_floor(self, qs, name, value):
        if value:
            return qs.exclude(floor=1).exclude(floor=F('max_floor'))
        return qs

    class Meta:
        model = Apartment
        fields = (
            'rooms', 'min_price', 'min_price', 'start_floor', 'last_floor',
            'year'
        )
