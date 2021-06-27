from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import UserAccount
from courses.models import Courses, Lessons, Comments, Replies, UserCourseAccess


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'name', 'isStaff', 'isAdmin']



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


class CourseStatusSerializer(ModelSerializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    slug = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=False)
    thumbnail = serializers.CharField(required=False)
    video = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    isPublished = serializers.BooleanField(required=True)


    class Meta:
        model = Courses
        fields = '__all__'


class GetCoursesOwnersSerializer(ModelSerializer):

    class Meta:
        model = UserCourseAccess
        fields = '__all__'


class GetCoursesSerializer(ModelSerializer):
    user_course = GetCoursesOwnersSerializer(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = ['id', 'title', 'slug', 'description', 'duration', 'thumbnail', 'video', 'price', 'purchases', 'user_course', 'lessons', 'isPublished', 'createdAt', 'updatedAt']


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


class GrantUserCourseAccessSerializer(ModelSerializer):

    class Meta:
        model = UserCourseAccess
        fields = '__all__'


class GetUserCoursesSerializer(ModelSerializer):
    course = GetCoursesSerializer(read_only=True, source='courseId')

    class Meta:
        model = UserCourseAccess
        fields = ['course']


class GetLessonsSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'


class PostCommentSerializer(ModelSerializer):
    comment = serializers.CharField(required=False)

    class Meta:
        model = Comments
        fields = '__all__'


class ReplyCommentSerializer(ModelSerializer):
    class Meta:
        model = Replies
        fields = '__all__'


class GetCommentReplySerializer(ModelSerializer):
    user = UserSerializer(read_only=True, source='userId')

    class Meta:
        model = Replies
        fields = ['commentId', 'user', 'comment', 'createdAt', 'updatedAt']


class GetCommentSerializer(ModelSerializer):
    replies = GetCommentReplySerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True, source='userId')

    class Meta:
        model = Comments
        fields = ['id', 'lessonId', 'user', 'comment', 'createdAt', 'updatedAt', 'replies']

