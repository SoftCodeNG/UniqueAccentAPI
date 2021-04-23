import random

from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.text import slugify


class Courses(models.Model):
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

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            if Courses.objects.filter(slug=slugify(self.title)).exists():
                self.slug = slugify(self.title) + str(datetime.now().timestamp())
            else:
                self.slug = slugify(self.title)
        super(Courses, self).save(*args, **kwargs)

