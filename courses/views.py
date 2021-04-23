from rest_framework.decorators import api_view
from rest_framework.response import Response

from courses.serializer import CreateCourseSerializer
from services.checkToken import authenticateToken, isStaff, isAdmin


@api_view(['POST'])
@authenticateToken
@isStaff
def create_course(request):
    serializer = CreateCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'code': Response.status_code,
        'errors': serializer.errors,
        'payload': serializer.data if len(serializer.errors) == 0 else None
    })
