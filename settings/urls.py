from django.urls import path

from settings.views import create_service, get_all_services, update_service, delete_service, create_testimonial

urlpatterns = [
    path('services/createService', create_service, name='createService'),
    path('services/updateService/<str:slug>', update_service, name='updateService'),
    path('services/deleteService/<str:slug>', delete_service, name='deleteService'),
    path('services/getAllServices', get_all_services, name='getAllServices'),
    path('testimonial/createTestimonial', create_testimonial, name='createTestimonial'),
]
