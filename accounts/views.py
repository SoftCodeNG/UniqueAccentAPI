from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from django.core.mail import send_mail

from accounts.serializers import RegistrationSerializer


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
