from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from services.checkToken import authenticateToken, isAdmin
from settings.models import Service
from settings.serializers import CreateServiceSerializer, GetServiceSerializer, CreateTestimonialSerializer


@api_view(['POST'])
# @authenticateToken
# @isAdmin
def create_service(request):
    serializer = CreateServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['PUT'])
# @authenticateToken
# @isAdmin
def update_service(request, slug):
    service = Service.objects.get(slug=slug)
    serializer = CreateServiceSerializer(service, many=False, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['DELETE'])
# @authenticateToken
# @isAdmin
def delete_service(request, slug):
    service = Service.objects.get(slug=slug)
    service.delete()

    return Response({
        'code': Response.status_code,
        'description': 'Service Deleted',
        'payload': None
    })


@api_view(['GET'])
def get_all_services(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    service = Service.objects.all().order_by('-updatedAt')
    service = paginator.paginate_queryset(service, request)
    serializer = GetServiceSerializer(service, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
# @authenticateToken
# @isAdmin
def create_testimonial(request):
    serializer = CreateTestimonialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['PUT'])
# @authenticateToken
# @isAdmin
def update_testimonial(request, testimony_id):
    service = Service.objects.get(pk=testimony_id)
    serializer = CreateTestimonialSerializer(service, many=False, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['DELETE'])
# @authenticateToken
# @isAdmin
def delete_testimonial(request, testimony_id):
    service = Service.objects.get(pk=testimony_id)
    service.delete()

    return Response({
        'code': Response.status_code,
        'description': 'Service Deleted',
        'payload': None
    })
