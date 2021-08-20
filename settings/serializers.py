from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from media.models import Media
from settings.models import Service, Testimonial, HomePageSlider


class CreateServiceSerializer(ModelSerializer):
    title = serializers.CharField(required=True)
    thumbnail = serializers.CharField(required=True)
    slug = serializers.CharField(required=False)
    isFeatured = serializers.BooleanField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Service
        fields = '__all__'


class GetServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class CreateTestimonialSerializer(ModelSerializer):
    name = serializers.CharField(required=True)
    title = serializers.CharField(required=False)
    avatar = serializers.CharField(required=False)
    isTextTestimonial = serializers.BooleanField(required=True)
    testimony = serializers.CharField(required=True)

    class Meta:
        model = Testimonial
        fields = '__all__'


class GetTestimonialSerializer(ModelSerializer):

    class Meta:
        model = Testimonial
        fields = '__all__'


class CreateHomePageSlider(ModelSerializer):
    image = serializers.CharField(required=False)

    class Meta:
        model = HomePageSlider
        fields = '__all__'


class GetHomePageSlider(ModelSerializer):

    class Meta:
        model = HomePageSlider
        fields = '__all__'
