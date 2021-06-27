from django.urls import path

from courses.views import create_course, get_courses, get_course_details, create_lesson, get_lessons_by_id, \
    get_lesson_detail, post_comment, get_comments_by_lesson_id, reply_comment, update_course, course_status, \
    update_lesson, search_courses, grant_user_course_access, get_user_courses, delete_lesson, get_published_courses, \
    search_published_courses

urlpatterns = [
    path('createCourse', create_course, name='createCourse'),
    path('updateCourse/<str:slug>', update_course, name='updateCourse'),
    path('changeCourseStatus/<str:slug>', course_status, name='publishCourse'),
    path('getCourses', get_courses, name='getCourses'),
    path('getPublishedCourses', get_published_courses, name='getPublishedCourses'),
    path('searchCourses/<str:value>', search_courses, name='searchCourses'),
    path('searchPublishedCourses/<str:value>', search_published_courses, name='searchCourses'),
    path('getCourseDetails/<str:slug>', get_course_details, name='getCourseDetails'),
    path('grantUserCourseAccess', grant_user_course_access, name='grantUserCourseAccess'),
    path('getUserCourses/<int:user_id>', get_user_courses, name='getUserCourses'),
    path('createLesson', create_lesson, name='createLesson'),
    path('updateLesson/<str:slug>', update_lesson, name='updateLesson'),
    path('deleteLesson/<str:slug>', delete_lesson, name='deleteLesson'),
    path('getCourseLessons/<str:course_slug>', get_lessons_by_id, name='getCourseLessons'),
    path('getLessonDetail/<str:slug>', get_lesson_detail, name='getLessonDetail'),
    path('createComment', post_comment, name='createComment'),
    path('getLessonComments/<int:lesson_id>', get_comments_by_lesson_id, name='getLessonComments'),
    path('replyComment', reply_comment, name='replyComment'),
]
