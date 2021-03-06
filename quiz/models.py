import datetime

from django.db import models

# Create your models here.
from django.utils.text import slugify


class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False)
    passCode = models.CharField(max_length=20, blank=True, null=True)
    organisation = models.CharField(max_length=100, blank=True, null=True)
    organisationLogo = models.CharField(max_length=100, blank=True, null=True)
    instruction = models.TextField(blank=False, null=False)
    duration = models.IntegerField(default=0, null=False)
    startDate = models.DateTimeField(default=datetime.datetime.now())
    endDate = models.DateTimeField(null=True, blank=True)
    question = models.IntegerField(default=0, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            if Quiz.objects.filter(slug=slugify(self.title)).exists():
                self.slug = slugify(self.title) + str(datetime.now().timestamp())
            else:
                self.slug = slugify(self.title)
        super(Quiz, self).save(*args, **kwargs)


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quizQuestions')
    questionNo = models.IntegerField(null=False)
    question = models.TextField(blank=False, null=False)
    maxScore = models.IntegerField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class CandidateData(models.Model):
    id = models.AutoField(primary_key=True)
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    candidateName = models.TextField(null=False)
    candidateNumber = models.TextField(null=False)
    passCode = models.FileField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    questionsId = models.ForeignKey(Questions, on_delete=models.CASCADE)
    candidateDataId = models.ForeignKey(CandidateData, on_delete=models.CASCADE)
    answer = models.FileField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
