from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from courses.models import Courses, Lessons


class CreateCourseSerializer(ModelSerializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    slug = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=True)
    thumbnail = serializers.CharField(required=True)
    video = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)

    class Meta:
        model = Courses
        fields = '__all__'


class GetCoursesSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class CreateLessonSerializer(ModelSerializer):
    title = serializers.CharField(required=True)
    slug = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=True)
    thumbnail = serializers.CharField(required=True)
    video = serializers.CharField(required=True)

    class Meta:
        model = Lessons
        fields = '__all__'


class GetLessonsSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'
