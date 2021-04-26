from django.urls import path

from courses.views import create_course, get_courses, get_courses_detail, create_lesson

urlpatterns = [
    path('createCourse', create_course, name='createCourse'),
    path('getCourses', get_courses, name='getCourses'),
    path('getCoursesDetail/<str:slug>', get_courses_detail, name='getCoursesDetail'),
    path('createLesson', create_lesson, name='createLesson'),
]
