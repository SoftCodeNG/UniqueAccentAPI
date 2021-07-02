from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from quiz.models import Quiz, Questions
from quiz.serializer import CreateQuizSerializer, GetAllQuizSerializer, CreateQuestionSerializer, GetQuestionSerializer
from services.checkToken import authenticateToken, isAdmin, isStaff


@api_view(['POST'])
@authenticateToken
@isAdmin
def create_quiz(request):
    serializer = CreateQuizSerializer(data=request.data)
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
def update_quiz(request, slug):
    quiz = Quiz.objects.get(slug=slug)
    serializer = CreateQuizSerializer(quiz, many=False, data=request.data)
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
def get_quiz(request):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    quiz = Quiz.objects.all().order_by('-updatedAt')
    quiz = paginator.paginate_queryset(quiz, request)
    serializer = GetAllQuizSerializer(quiz, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_public_quiz(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    quiz = Quiz.objects.filter(passCode=None).order_by('-updatedAt')
    quiz = paginator.paginate_queryset(quiz, request)
    serializer = GetAllQuizSerializer(quiz, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@isStaff
def search_quiz(request, value):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    quiz = Quiz.objects.filter(title__icontains=value).filter(organisation__icontains=value).order_by('-updatedAt')
    quiz = paginator.paginate_queryset(quiz, request)
    serializer = GetAllQuizSerializer(quiz, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def search_public_quiz(request, value):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    quiz = Quiz.objects.filter(passCode=None).filter(title__icontains=value).order_by('-updatedAt')
    quiz = paginator.paginate_queryset(quiz, request)
    serializer = GetAllQuizSerializer(quiz, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_quiz_details(request, slug):
    quiz = Quiz.objects.get(slug=slug).select_related('quiz')
    serializer = GetAllQuizSerializer(quiz, many=False)
    return Response({
        'code': Response.status_code,
        'description': 'Quiz detail',
        'payload': serializer.data
    })


@api_view(['POST'])
@authenticateToken
@isAdmin
def create_question(request):
    serializer = CreateQuestionSerializer(data=request.data)
    if serializer.is_valid():
        quiz = Quiz.objects.get(slug=request.data['quizId'])
        quiz.question = int(quiz.question) + 1
        quiz.save()
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['PUT'])
@authenticateToken
@isAdmin
def update_question(request, quiz_id):
    question = Questions.objects.get(quizId=quiz_id)
    serializer = CreateQuestionSerializer(question, many=False, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['GET'])
def get_question_detail(request, question_id):
    lesson = Questions.objects.get(id=question_id)
    serializer = GetQuestionSerializer(lesson, many=False)
    return Response({
        'code': Response.status_code,
        'description': 'Question detail',
        'payload': serializer.data
    })


@api_view(['DELETE'])
@authenticateToken
@isAdmin
def delete_question(request, question_id):
    lesson = Questions.objects.get(id=question_id)
    lesson.delete()
    return Response({
        'code': Response.status_code,
        'description': 'Question deleted successfully',
        'payload': 'Question deleted successfully'
    })
