from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.name})
        data.update({'id': self.user.id})
        data.update({'lastLogin': self.user.last_login})
        data.update({'isStaff': self.user.isStaff})
        data.update({'isAdmin': self.user.isAdmin})
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email
        token['lastLogin'] = user.last_login
        token['isStaff'] = user.isStaff
        token['isAdmin'] = user.isAdmin
        return token

