from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from courses.models import Courses, Lessons, Comments, Replies


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


class PostCommentSerializer(ModelSerializer):
    comment = serializers.CharField(required=False)

    class Meta:
        model = Comments
        fields = '__all__'


class GetCommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class ReplyCommentSerializer(ModelSerializer):
    comment = serializers.CharField(required=False)

    class Meta:
        model = Replies
        fields = '__all__'
