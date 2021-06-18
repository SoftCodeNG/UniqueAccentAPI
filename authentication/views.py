from datetime import datetime

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.models import UserAccount
from authentication.serializer import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            email = request.data['email']
            user = UserAccount.objects.get(email=email)
            user.last_login = datetime.now()
            user.save()
        return response
    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()
