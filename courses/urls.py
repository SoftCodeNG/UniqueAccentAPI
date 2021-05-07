from django.urls import path

from courses.views import create_course, get_courses, get_course_details, create_lesson, get_lessons_by_id, \
    get_lesson_detail

urlpatterns = [
    path('createCourse', create_course, name='createCourse'),
    path('getCourses', get_courses, name='getCourses'),
    path('getCourseDetails/<str:slug>', get_course_details, name='getCourseDetails'),
    path('createLesson', create_lesson, name='createLesson'),
    path('getCourseLessons/<int:course_id>', get_lessons_by_id, name='getCourseLessons'),
    path('getLessonDetail/<str:slug>', get_lesson_detail, name='getLessonDetail'),
]
