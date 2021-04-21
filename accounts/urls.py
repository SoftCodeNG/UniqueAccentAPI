from django.urls import path

from accounts.views import registration_view

urlpatterns = [
    path('register', registration_view, name='register'),
]
