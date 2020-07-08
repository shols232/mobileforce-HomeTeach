from django.conf import settings
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(required=False, default='', allow_blank=True)
    last_name = serializers.CharField(required=False, default='', allow_blank=True)

    class Meta:
        model = User
        fields = ['email','is_tutor', 'password','first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']

        user = User.objects.create_user(

            email=self.validated_data['email'],

        )
        user.is_tutor = self.validated_data['is_tutor']
        try:
            user.first_name = self.validated_data['first_name']
        except KeyError:
            user.first_name = ''
        try:
            user.last_name = self.validated_data['last_name']
        except KeyError:
            user.last_name = ''
        user.set_password(password)
        user.save()
        return user