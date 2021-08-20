from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime
from django.utils.text import slugify


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False)
    thumbnail = models.CharField(max_length=500, null=False)
    isFeatured = models.BooleanField(default=False, null=False)
    description = models.TextField(blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            if Service.objects.filter(slug=slugify(self.title)).exists():
                self.slug = slugify(self.title) + str(datetime.now().timestamp())
            else:
                self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)


class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.SlugField(max_length=100)
    avatar = models.CharField(max_length=500)
    isTextTestimonial = models.BooleanField(default=True, null=False)
    testimony = models.TextField(blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class HomePageSlider(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=500, null=False)
