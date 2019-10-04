from rest_framework import serializers

from apps.apartment.models import Apartment


class ApartmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = "__all__"
