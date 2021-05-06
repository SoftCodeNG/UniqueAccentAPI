from django.urls import path
from media.views import upload_media, delete_media, get_all_media, get_all_images, get_all_videos, get_all_audio

urlpatterns = [
    path('uploadMedia', upload_media, name='uploadMedia'),
    path('getAllMedia', get_all_media, name='getAllMedia'),
    path('getAllImages', get_all_images, name='getAllImages'),
    path('getAllVideo', get_all_videos, name='getAllVideo'),
    path('getAllAudio', get_all_audio, name='getAllAudio'),
    path('deleteMedia/<pk>', delete_media, name='deleteMedia'),
]
