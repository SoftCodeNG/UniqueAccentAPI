from django.urls import path

from quiz.views import create_quiz, update_quiz, get_quiz, get_public_quiz, search_quiz, search_public_quiz, \
    get_quiz_details, create_question, update_question, get_question_detail, delete_question

urlpatterns = [
    path('createQuiz', create_quiz, name='createQuiz'),
    path('updateQuiz/<str:value>', update_quiz, name='updateQuiz'),
    path('getQuiz', get_quiz, name='getQuiz'),
    path('getPublicQuiz', get_public_quiz, name='getPublicQuiz'),
    path('getQuiz/<str:value>', search_quiz, name='searchQuiz'),
    path('getPublicQuiz/<str:value>', search_public_quiz, name='searchPublicQuiz'),
    path('getQuizDetails/<str:slug>', get_quiz_details, name='getQuizDetails'),
    path('createQuestion', create_question, name='createQuestion'),
    path('updateQuestion/<int:quiz_id>', update_question, name='updateQuestion'),
    path('getQuestionDetail/<int:question_id>', get_question_detail, name='getQuestionDetail'),
    path('deleteQuestion/<int:question_id>', delete_question, name='deleteQuestion'),
]
