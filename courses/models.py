import random

from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.text import slugify
from accounts.models import UserAccount


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    duration = models.IntegerField(default=0, null=False)
    thumbnail = models.CharField(max_length=500, null=False)
    video = models.CharField(max_length=500, null=False)
    price = models.DecimalField(max_digits=11, decimal_places=3, null=False)
    purchases = models.IntegerField(default=0, null=False)
    lessons = models.IntegerField(default=0, null=False)
    isPublished = models.BooleanField(default=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            if Courses.objects.filter(slug=slugify(self.title)).exists():
                self.slug = slugify(self.title) + str(datetime.now().timestamp())
            else:
                self.slug = slugify(self.title)
        super(Courses, self).save(*args, **kwargs)


class UserCourseAccess(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    courseId = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='user_course')
    isPurchased = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Lessons(models.Model):
    id = models.AutoField(primary_key=True)
    courseSlug = models.ForeignKey(Courses, to_field='slug', on_delete=models.CASCADE, related_name='course_lesson')
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    duration = models.IntegerField(default=0, null=False)
    thumbnail = models.CharField(max_length=500, null=False)
    video = models.CharField(max_length=500, null=False)
    views = models.IntegerField(default=0, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            if Lessons.objects.filter(slug=slugify(self.title)).exists():
                self.slug = slugify(self.title) + str(datetime.now().timestamp())
            else:
                self.slug = slugify(self.title)
        super(Lessons, self).save(*args, **kwargs)


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    lessonId = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    userId = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    comment = models.TextField(blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Replies(models.Model):
    id = models.AutoField(primary_key=True)
    commentId = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='replies')
    userId = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    comment = models.TextField(blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
