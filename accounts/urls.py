from django.urls import path

from accounts.views import registration_view, staff_registration_view, admin_registration_view

urlpatterns = [
    path('register', registration_view, name='register'),
    path('registerStaff', staff_registration_view, name='registerStaff'),
    path('registerAdmin', admin_registration_view, name='registerAdmin'),
]
