from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from media.models import Media


class UploadMediaSerializer(ModelSerializer):
    name = serializers.CharField(required=False)
    fileFormat = serializers.CharField(required=False)
    fileType = serializers.CharField(required=False)
    fileSizeInKB = serializers.CharField(required=False)
    uploadedOn = serializers.DateTimeField(required=False)

    class Meta:
        model = Media
        fields = '__all__'


class GetUserMediaSerializer(ModelSerializer):

    class Meta:
        model = Media
        fields = '__all__'
