from rest_framework.serializers import ModelSerializer
from accounts.models import UserAccount


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['email', 'name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = UserAccount(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
            password=self.validated_data['password']
        )

        account.set_password(self.validated_data['password'])
        account.save()
        return account
