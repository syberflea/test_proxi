from rest_framework import mixins, status, viewsets

from .models import Owner, Client
from .serializers import OwnerSerializer, ClientSerializer, UpdateClientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientAPIView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateClientViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """
    Создание объекта клиента без JWT.
    """
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()


class RetrieveClientViewSet(
    mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Получение объекта клиента.
    """
    queryset = Client.objects.all()
    # TODO отредактировать сериалайзер
    serializer_class = ClientSerializer
    # TODO написать кастомный пермишн, получить сведения только о себе
    permission_classes = [AllowAny]
    # TODO подключить кастомную авторизацию по JWT
    # authentication_classes = [TokenAuthentication]
    

class UpdateClientViewSet(
    mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    Обновление объекта клиента.
    """
    queryset = Client.objects.all()
    # отрудактировать сериалайзер
    serializer_class = UpdateClientSerializer
    # настроить разрешение только для себя
    permission_classes = [AllowAny]
    # TODO подключить кастомную авторизацию по JWT
    # authentication_classes = [TokenAuthentication]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)  # это лишнее?
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
