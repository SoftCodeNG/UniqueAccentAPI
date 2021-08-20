from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from services.checkToken import authenticateToken, isAdmin
from settings.models import Service, Testimonial, HomePageSlider
from settings.serializers import CreateServiceSerializer, GetServiceSerializer, CreateTestimonialSerializer, \
    GetTestimonialSerializer, CreateHomePageSlider, GetHomePageSlider


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


@api_view(['GET'])
def get_all_testimonials(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    testimonial = Testimonial.objects.all().order_by('-updatedAt')
    testimonial = paginator.paginate_queryset(testimonial, request)
    serializer = GetTestimonialSerializer(testimonial, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['PUT'])
# @authenticateToken
# @isAdmin
def update_testimonial(request, testimony_id):
    testimonial = Testimonial.objects.get(id=testimony_id)
    serializer = CreateTestimonialSerializer(testimonial, many=False, data=request.data)
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
    testimonial = Testimonial.objects.get(pk=testimony_id)
    testimonial.delete()

    return Response({
        'code': Response.status_code,
        'description': 'Testimonial Deleted',
        'payload': None
    })


@api_view(['POST'])
# @authenticateToken
# @isAdmin
def add_home_page_slider(request):
    serializer = CreateHomePageSlider(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })


@api_view(['GET'])
def get_all_home_page_slider(request):
    paginator = PageNumberPagination()
    paginator.page_size = 100
    home_page_slider = HomePageSlider.objects.all()
    home_page_slider = paginator.paginate_queryset(home_page_slider, request)
    serializer = GetHomePageSlider(home_page_slider, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['DELETE'])
# @authenticateToken
# @isAdmin
def delete_home_page_slider(request, slider_id):
    home_page_slider = HomePageSlider.objects.get(pk=slider_id)
    home_page_slider.delete()

    return Response({
        'code': Response.status_code,
        'description': 'Home Page Slider Deleted',
        'payload': None
    })
