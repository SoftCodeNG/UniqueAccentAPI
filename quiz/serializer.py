from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from quiz.models import Quiz, Questions, Answers, CandidateData


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


class GetQuestionSerializer(ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'


class GetAllQuizSerializer(ModelSerializer):
    quizQuestions = GetQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'slug', 'passCode', 'organisation', 'organisationLogo', 'instruction',
                  'duration', 'startDate', 'endDate', 'question', 'quizQuestions', 'createdAt', 'updatedAt']


class CreateQuestionSerializer(ModelSerializer):
    questionNo = serializers.IntegerField(required=True)
    question = serializers.CharField(required=True)
    maxScore = serializers.IntegerField(required=True)

    class Meta:
        model = Questions
        fields = '__all__'


class RegisterCandidateSerializer(ModelSerializer):
    quizId = serializers.IntegerField(required=True)
    candidateName = serializers.CharField(required=True)
    candidateNumber = serializers.CharField(required=True)
    passCode = serializers.CharField(required=True)

    class Meta:
        model = CandidateData
        fields = '__all__'


class GetAllCandidateForAQuizSerializer(ModelSerializer):

    class Meta:
        model = CandidateData
        fields = '__all__'


class PostAnswerSerializer(ModelSerializer):
    questionsId = serializers.IntegerField(required=True)
    candidateDataId = serializers.IntegerField(required=True)
    answer = serializers.FileField(required=True)

    class Meta:
        model = Answers
        fields = '__all__'
