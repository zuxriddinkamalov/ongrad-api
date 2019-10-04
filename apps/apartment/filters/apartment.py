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

    class Meta:
        model = Apartment
        fields = (
            'rooms', 'min_price', 'min_price', 'floor', 'year'
        )