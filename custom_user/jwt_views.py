# from django.contrib.auth import get_user_model
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Client
from .serializers import ClientSerializer
from .utils import generate_access_token, generate_refresh_token


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    # Client = get_user_model()
    email = request.data.get('email')
    password = request.data.get('password')
    response = Response()
    if (email is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'email and password required')

    client = Client.objects.filter(email=email).first()
    if client is None:
        raise exceptions.AuthenticationFailed('client not found')
    # почему при создании пароль не устанавливается через сет пасворд?!
    # Проверить как работае функция check_password
    if not client.check_password(password):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_client = ClientSerializer(client).data

    access_token = generate_access_token(client)
    refresh_token = generate_refresh_token(client)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_client,
    }

    return response
