from django.urls import path

from settings.views import create_service

urlpatterns = [
    path('services', create_service, name='services'),
]
