import random
import string

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import RegistrationSerializer, StaffRegistrationSerializer, AdminRegistrationSerializer
from services.checkToken import isAdmin
from django.contrib.auth import get_user_model
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
    print(data)

    if 'error' in data:
        content = {'message': 'wrong google token / this google token is already expired.'}
        return Response(content)

    # create user if not exist
    try:
        user = User.objects.get(email=data['email'])
    except User.DoesNotExist:
        # provider random default password
        # lower = string.ascii_lowercase
        # upper = string.ascii_uppercase
        # num = string.digits
        # symbols = string.punctuation
        # all = lower + upper + num + symbols
        # temp = random.sample(all, 10)
        # password = "".join(temp)
        # print(password)

        user = User()
        user.password = make_password(BaseUserManager().make_random_password())
        user.name = request.data.get("name")
        user.email = data['email']
        user.save()

    token = RefreshToken.for_user(user)  # generate token without username & password
    response = {}
    # response['username'] = user.username
    response['access'] = str(token.access_token)
    response['refresh'] = str(token)
    response['isAdmin'] = user.isAdmin
    response['isStaff'] = user.isStaff
    response['lastLogin'] = user.last_login
    response['user'] = user.name
    return Response(response)
