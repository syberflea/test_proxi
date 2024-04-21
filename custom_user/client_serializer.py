from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from typing import Any, Dict, Optional, Type, TypeVar
from django.contrib.auth.models import AbstractBaseUser, update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from .models import UserAccount
from rest_framework.exceptions import AuthenticationFailed


# class ClientTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         # Дополнительная логика, если нужно
#         return data


class ClientTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user  # Получаем пользователя

        # Ваша логика для обработки клиентского пользователя
        # Например, проверка, является ли пользователь клиентом (тип - CLIENT)
        if user.type != UserAccount.Types.CLIENT:
            raise AuthenticationFailed("Authentication failed. Not a client.")

        return data


class ClientTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Дополнительная логика, если нужно
        return data
