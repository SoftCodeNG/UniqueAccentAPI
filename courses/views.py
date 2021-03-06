from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.decorators import api_view
from rest_framework.response import Response

from courses.models import Courses, Lessons, Comments, UserCourseAccess
from courses.serializer import CreateCourseSerializer, CreateLessonSerializer, GetCoursesSerializer, \
    GetLessonsSerializer, PostCommentSerializer, GetCommentSerializer, ReplyCommentSerializer, CourseStatusSerializer, \
    GetUserCoursesSerializer, GrantUserCourseAccessSerializer
from accounts.models import UserAccount
from services.checkToken import authenticateToken, isAdmin, isStaff
from rest_framework.pagination import PageNumberPagination

from services.sendEmail import send_purchase_confirmation


@api_view(['POST'])
@authenticateToken
@isAdmin
def create_course(request):
    serializer = CreateCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['PUT'])
@authenticateToken
@isAdmin
def update_course(request, slug):
    course = Courses.objects.get(slug=slug)
    serializer = CreateCourseSerializer(course, many=False, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['PUT'])
@authenticateToken
@isAdmin
def course_status(request, slug):
    course = Courses.objects.get(slug=slug)
    serializer = CourseStatusSerializer(course, many=False, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['GET'])
@authenticateToken
@isStaff
def get_courses(request):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    courses = Courses.objects.all().order_by('-updatedAt').prefetch_related('user_course')
    courses = paginator.paginate_queryset(courses, request)
    serializer = GetCoursesSerializer(courses, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_published_courses(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    courses = Courses.objects.filter(isPublished=True).order_by('-updatedAt')
    courses = paginator.paginate_queryset(courses, request)
    serializer = GetCoursesSerializer(courses, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_courses_for_homepage(request):
    paginator = PageNumberPagination()
    paginator.page_size = 3
    courses = Courses.objects.filter(isPublished=True).order_by('-createdAt')
    courses = paginator.paginate_queryset(courses, request)
    serializer = GetCoursesSerializer(courses, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@isStaff
def search_courses(request, value):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    courses = Courses.objects.filter(title__icontains=value).order_by('-updatedAt')
    courses = paginator.paginate_queryset(courses, request)
    serializer = GetCoursesSerializer(courses, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def search_published_courses(request, value):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    courses = Courses.objects.filter(isPublished=True).filter(title__icontains=value).order_by('-updatedAt')
    courses = paginator.paginate_queryset(courses, request)
    serializer = GetCoursesSerializer(courses, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_course_details(request, slug):
    course = Courses.objects.get(slug=slug)
    serializer = GetCoursesSerializer(course, many=False)
    return Response({
        'code': Response.status_code,
        'description': 'Courses detail',
        'payload': serializer.data
    })


@api_view(['POST'])
@authenticateToken
def grant_user_course_access(request):
    check_if_access_is_already_granted = UserCourseAccess.objects.filter(userId=request.data['userId'], courseId=request.data['courseId'])

    if not check_if_access_is_already_granted:
        serializer = GrantUserCourseAccessSerializer(data=request.data)
        if serializer.is_valid():
            # if request.data['isPurchased']:
            #     course = Courses.objects.get(pk=request.data['courseId'])
            #     user = UserAccount.objects.get(pk=request.data['userId'])
            #     Courses.objects.filter(pk=request.data['courseId']).update(purchases=course.purchases + 1)
            #     html_message = send_purchase_confirmation(user.name, user.email, course.title)
            #     plain_message = strip_tags(html_message)
            #     send_mail(
            #         'Thanks for your purchase',
            #         plain_message,
            #         'noreply@uniqueaccent.com.ng',
            #         [user.email],
            #         html_message=html_message
            #     )
            serializer.save()
        return Response({
            'code': Response.status_code,
            'description': 'User Assigned to course',
            'payload': serializer.data
        })
    else:
        return Response({
            'code': Response.status_code,
            'description': 'Already assigned to course',
            'payload': None
        })


@api_view(['GET'])
@authenticateToken
def get_user_courses(request, user_id):
    user_course = UserCourseAccess.objects.order_by('-updatedAt').filter(userId=user_id).select_related('courseId')
    serializer = GetUserCoursesSerializer(user_course, many=True)

    all_user_courses = []
    for x in serializer.data:
        all_user_courses.append(x['course'])

    return Response({
        'code': Response.status_code,
        'description': 'List of all user courses',
        'payload': all_user_courses
    })


@api_view(['POST'])
@authenticateToken
@isAdmin
def create_lesson(request):
    serializer = CreateLessonSerializer(data=request.data)
    if serializer.is_valid():
        course = Courses.objects.get(slug=request.data['courseSlug'])
        course.lessons = int(course.lessons) + 1
        course.duration = course.duration + int(course.duration)
        course.save()
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['PUT'])
@authenticateToken
@isAdmin
def update_lesson(request, slug):
    lesson = Lessons.objects.get(slug=slug)
    serializer = CreateLessonSerializer(lesson, many=False, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['DELETE'])
@authenticateToken
@isAdmin
def delete_lesson(request, slug):
    lesson = Lessons.objects.get(slug=slug)
    lesson.delete()
    return Response({
        'code': Response.status_code,
        'description': 'Lesson deleted successfully',
        'payload': 'Lesson deleted successfully'
    })


@api_view(['GET'])
def get_lessons_by_id(request, course_slug):
    lessons = Lessons.objects.filter(courseSlug=course_slug)
    serializer = GetLessonsSerializer(lessons, many=True)
    return Response({
        'code': Response.status_code,
        'description': 'All lessons for a course',
        'payload': serializer.data
    })


@api_view(['GET'])
def get_lesson_detail(request, slug):
    lesson = Lessons.objects.get(slug=slug)
    serializer = GetLessonsSerializer(lesson, many=False)
    return Response({
        'code': Response.status_code,
        'description': 'Lesson detail',
        'payload': serializer.data
    })


@api_view(['Post'])
@authenticateToken
def post_comment(request):
    serializer = PostCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['GET'])
@authenticateToken
def get_comments_by_lesson_id(request, lesson_id):
    comments = Comments.objects.filter(lessonId=lesson_id).order_by('-updatedAt').select_related(
        'userId').prefetch_related('replies')
    serializer = GetCommentSerializer(comments, many=True)
    return Response({
        'code': Response.status_code,
        'description': 'All Comments for a lesson',
        'payload': serializer.data
    })


@api_view(['Post'])
@authenticateToken
def reply_comment(request):
    serializer = ReplyCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })
