from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken, Token

from accounts.models import UserAccount
from accounts.serializers import RegistrationSerializer, StaffRegistrationSerializer, AdminRegistrationSerializer
from services.checkToken import isAdmin
from django.contrib.auth import get_user_model

from services.sendEmail import send_reset_password_email

User = get_user_model()


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        request_serializer = RegistrationSerializer(data=request.data)
        data = {}
        if request_serializer.is_valid():
            account = request_serializer.save()
            # r = requests.post('http://127.0.0.1:8000/auth/token/', json={'email': account.email, 'password': request.data['password']})
            # if r.status_code == 200:
            #     print('I am here')
            #     send_mail(
            #         'Thanks for Registering',
            #         f'''
            #             Hi {account.name},
            #             I'm the creator of the BizPage. Our goal is to help you with optimization and increase your sales in Instagram. Thanks for registering with our service! We hope that your business will grow even faster.
            #
            #             Your email: {account.email}
            #             Your password: ********* (Hidden)
            #
            #             Using BizPage is easy so have a happy sales.
            #             ''',
            #         'austineforall@gmail.com',
            #         [account.email]
            #         # False, None, None, None, True
            #     )
            #     return Response(r.json())
            # else:
            #     print(r)
            return Response(request_serializer.data)
        else:
            return Response(request_serializer.errors)


@api_view(['POST'])
# @isAdmin
def staff_registration_view(request):
    if request.method == 'POST':
        request_serializer = StaffRegistrationSerializer(data=request.data)
        data = {}
        if request_serializer.is_valid():
            account = request_serializer.save()
            # r = requests.post('http://127.0.0.1:8000/auth/token/', json={'email': account.email, 'password': request.data['password']})
            # if r.status_code == 200:
            #     print('I am here')
            #     send_mail(
            #         'Thanks for Registering',
            #         f'''
            #             Hi {account.name},
            #             I'm the creator of the BizPage. Our goal is to help you with optimization and increase your sales in Instagram. Thanks for registering with our service! We hope that your business will grow even faster.
            #
            #             Your email: {account.email}
            #             Your password: ********* (Hidden)
            #
            #             Using BizPage is easy so have a happy sales.
            #             ''',
            #         'austineforall@gmail.com',
            #         [account.email]
            #         # False, None, None, None, True
            #     )
            #     return Response(r.json())
            # else:
            #     print(r)
            return Response(request_serializer.data)
        else:
            return Response(request_serializer.errors)


@api_view(['POST'])
# @isAdmin
def admin_registration_view(request):
    if request.method == 'POST':
        request_serializer = AdminRegistrationSerializer(data=request.data)
        data = {}
        if request_serializer.is_valid():
            account = request_serializer.save()
            # r = requests.post('http://127.0.0.1:8000/auth/token/', json={'email': account.email, 'password': request.data['password']})
            # if r.status_code == 200:
            #     print('I am here')
            #     send_mail(
            #         'Thanks for Registering',
            #         f'''
            #             Hi {account.name},
            #             I'm the creator of the BizPage. Our goal is to help you with optimization and increase your sales in Instagram. Thanks for registering with our service! We hope that your business will grow even faster.
            #
            #             Your email: {account.email}
            #             Your password: ********* (Hidden)
            #
            #             Using BizPage is easy so have a happy sales.
            #             ''',
            #         'austineforall@gmail.com',
            #         [account.email]
            #         # False, None, None, None, True
            #     )
            #     return Response(r.json())
            # else:
            #     print(r)
            return Response(request_serializer.data)
        else:
            return Response(request_serializer.errors)


@api_view(['POST'])
def login_with_google(request):
    payload = {'access_token': request.data.get("token")}  # validate the token
    r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
    data = json.loads(r.text)

    if 'error' in data:
        content = {'message': 'wrong google token / this google token is already expired.'}
        return Response(content)

    # create user if not exist
    try:
        user = User.objects.get(email=data['email'])
        user.last_login = datetime.now()
        user.save()
    except User.DoesNotExist:
        user = User()
        user.password = make_password(BaseUserManager().make_random_password())
        user.name = request.data.get("name")
        user.email = data['email']
        user.last_login = datetime.now()
        user.save()

    token = RefreshToken.for_user(user)  # generate token without username & password
    response = {
        'access': str(token.access_token),
        'refresh': str(token),
        'isAdmin': user.isAdmin,
        'isStaff': user.isStaff,
        'lastLogin': user.last_login,
        'user': user.name
    }
    return Response(response)


@api_view(['POST'])
def forget_password(request):
    user_account = UserAccount.objects.get(email__exact=request.data.get('email'))
    token = RefreshToken.for_user(user_account)

    send_mail(
        'Password Reset Confirmation',
        send_reset_password_email(token),
        'austineforall@gmail.com',
        [request.data.get('email')]
    )
    print(token)

    return Response({
        'description': 'A resent link was sent to your email.'
    })
