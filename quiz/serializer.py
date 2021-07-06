from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from quiz.models import Quiz, Questions


class CreateQuizSerializer(ModelSerializer):
    title = serializers.CharField(required=True)
    slug = serializers.CharField(required=False)
    instruction = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)
    startDate = serializers.DateTimeField(required=True)
    endDate = serializers.DateTimeField(required=True)

    class Meta:
        model = Quiz
        fields = '__all__'


class GetAllQuizSerializer(ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'


class CreateQuestionSerializer(ModelSerializer):
    quizId = serializers.IntegerField(required=True)
    questionNo = serializers.IntegerField(required=True)
    question = serializers.CharField(required=True)
    maxScore = serializers.IntegerField(required=True)

    class Meta:
        model = Questions
        fields = '__all__'


class GetQuestionSerializer(ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'
