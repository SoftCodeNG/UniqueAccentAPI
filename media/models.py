from django.core.validators import MaxValueValidator
from django.db import models
from accounts.models import UserAccount


def user_directory_path(instance, filename):
    return f'{instance.fileType.lower()}/{filename}'


class Media(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to=user_directory_path)
    fileFormat = models.CharField(max_length=8)
    fileType = models.CharField(max_length=10)
    fileSizeInKB = models.CharField(max_length=10)
    uploadedOn = models.DateTimeField(auto_now_add=True)

