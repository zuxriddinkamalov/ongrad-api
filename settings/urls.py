from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', include_docs_urls(title='Ongrad API')),
    path('admin/', admin.site.urls),
    path('api/v1/',
         include('apps.apartment.urls', namespace='apps.apartment')),
]
