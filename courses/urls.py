from django.urls import path

from courses.views import create_course

urlpatterns = [
    path('createCourse', create_course, name='createCourse'),
]
