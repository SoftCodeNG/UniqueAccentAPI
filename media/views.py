import os

from rest_framework.decorators import api_view
from rest_framework.response import Response

from media.models import Media
from media.serializers import UploadMediaSerializer, GetUserMediaSerializer
from services.checkToken import authenticateToken


@api_view(['POST'])
# @authenticateToken
def upload_media(request):
    data = request.data
    file = request.FILES

    print('This is the size', file['file'].size)
    data['name'] = file['file'].name
    data['fileSizeInKB'] = str(file['file'].size / 1000)
    data['fileFormat'] = '.' + file['file'].name.split('.')[-1]
    data['fileType'] = file['file'].content_type.split('/')[0]

    if data['fileType'] == 'application':
        return Response({
            'code': Response.status_code,
            'description': 'Invalid File Type. Try uploading image, video or audio',
            'errors': ['File type is invalid'],
            'hasErrors': True,
            'success': False,
            'payload': None
        })
    serializer = UploadMediaSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'description': 'Media Uploaded',
        'errors': serializer.errors,
        'hasErrors': True if len(serializer.errors) > 0 else False,
        'success': False if len(serializer.errors) > 0 else True,
        'payload': serializer.data
    })


@api_view(['GET'])
# @authenticateToken
def get_all_media(request):
    media = Media.objects.all()
    serializer = GetUserMediaSerializer(media, many=True)

    return Response({
        'code': Response.status_code,
        'description': 'All Media',
        'payload': serializer.data
    })


@api_view(['GET'])
# @authenticateToken
def get_all_images(request):
    media = Media.objects.filter(fileType__exact='image')
    serializer = GetUserMediaSerializer(media, many=True)

    return Response({
        'code': Response.status_code,
        'description': 'All Images',
        'payload': serializer.data
    })


@api_view(['GET'])
# @authenticateToken
def get_all_videos(request):
    media = Media.objects.filter(fileType__exact='video')
    serializer = GetUserMediaSerializer(media, many=True)

    return Response({
        'code': Response.status_code,
        'description': 'All Videos',
        'payload': serializer.data
    })


@api_view(['GET'])
@authenticateToken
def get_single_media(request, jwtDecode, pk):
    media = Media.objects.filter(user_id__exact=jwtDecode['user_id']).get(id=pk)
    serializer = GetUserMediaSerializer(media, many=False)

    return Response({
        'code': Response.status_code,
        'description': 'All Messages',
        'payload': serializer.data
    })


@api_view(['DELETE'])
@authenticateToken
def delete_media(request, jwtDecode, pk):
    media = Media.objects.filter(user_id__exact=jwtDecode['user_id']).get(id=pk)
    path = media.file.path
    print(os.path.isfile(path))
    if os.path.isfile(path):
        os.remove(str(path))
        media.delete()
        return Response({
            'code': Response.status_code,
            'description': 'File Deleted',
            'payload': None
        })
    else:
        return Response({
            'code': Response.status_code,
            'description': 'No file found',
            'error': ['No file found'],
            'payload': None
        })
