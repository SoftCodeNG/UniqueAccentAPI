from rest_framework.decorators import api_view
from rest_framework.response import Response

from courses.models import Courses, Lessons, Comments
from courses.serializer import CreateCourseSerializer, CreateLessonSerializer, GetCoursesSerializer, \
    GetLessonsSerializer, PostCommentSerializer, GetCommentSerializer, ReplyCommentSerializer
from accounts.models import UserAccount
from services.checkToken import authenticateToken, isAdmin


@api_view(['POST'])
# @authenticateToken
# @isAdmin
def create_course(request):
    serializer = CreateCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['GET'])
def get_courses(request):
    courses = Courses.objects.all()
    serializer = GetCoursesSerializer(courses, many=True)
    return Response({
        'code': Response.status_code,
        'description': 'All courses',
        'payload': serializer.data
    })


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
def create_lesson(request):
    serializer = CreateLessonSerializer(data=request.data)
    if serializer.is_valid():
        course = Courses.objects.get(pk=request.data['courseSlug'])
        course.lessons = int(course.lessons) + 1
        course.save()
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['GET'])
def get_lessons_by_id(request, course_id):
    lessons = Lessons.objects.filter(courseId=course_id)
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
def get_comments_by_lesson_id(request, lesson_id):
    comments = Comments.objects.filter(lessonId=lesson_id).prefetch_related('replies')
    serializer = GetCommentSerializer(comments, many=True)
    return Response({
        'code': Response.status_code,
        'description': 'All Comments for a lesson',
        'payload': serializer.data
    })


@api_view(['Post'])
def reply_comment(request):
    serializer = ReplyCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })
