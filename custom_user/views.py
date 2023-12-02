from rest_framework import mixins, status, viewsets

from .models import Owner, Client
from .serializers import OwnerSerializer, ClientSerializer
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


# class CreateClientViewSet(viewsets.ViewSet):
#     """
#     Создание объекта клиента. Не в полной мере распознается swagger.
#     """
#     def create(self, request):
#         serializer = ClientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer



# class CreateClientViewSet(
#     mixins.CreateModelMixin, viewsets.GenericViewSet
# ):
#     """
#     Создание объекта клиента с использованием миксинов.
#     """
#     serializer_class = ClientSerializer  # Указываем используемый сериализатор
#     # authentication_classes = [TokenAuthentication]  # Установка класса аутентификации
#     permission_classes = [AllowAny]  # Установка класса разрешений


class CreateClientViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """
    Создание объекта клиента с использованием миксинов.
    """
    serializer_class = ClientSerializer  # Указываем используемый сериализатор
    permission_classes = [AllowAny]  # Установка класса разрешений

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
