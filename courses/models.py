from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    duration = models.IntegerField(default=0, null=False)
    image = models.ImageField(null=False)
    video = models.FileField(null=False)
    price = models.DecimalField(null=False)
    purchases = models.IntegerField(default=0, null=False)

