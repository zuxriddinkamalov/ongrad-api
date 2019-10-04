from django.urls import path, include
from rest_framework import routers

from .views import ApartmentViewSet

app_name = 'apps.apartment'

router = routers.DefaultRouter()
router.register(r'apartment', ApartmentViewSet, base_name='apartment')

urlpatterns = [
    path('', include(router.urls)),
]
