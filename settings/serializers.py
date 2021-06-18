from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from media.models import Media
from settings.models import Service


class CreateServiceSerializer(ModelSerializer):
    title = serializers.CharField(required=True)
    thumbnail = serializers.CharField(required=True)
    isFeatured = serializers.BooleanField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Service
        fields = '__all__'


class GetServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
