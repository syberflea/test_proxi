from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, ClientViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .client_serializer import (
    ClientTokenObtainPairSerializer,
    ClientTokenRefreshSerializer)
from .owner_serializer import (
    OwnerTokenObtainPairSerializer,
    OwnerTokenRefreshSerializer
)

class ClientTokenObtainPairView(TokenObtainPairView):
    serializer_class = ClientTokenObtainPairSerializer


router = DefaultRouter()

router.register('owner', OwnerViewSet)
router.register('client', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api/token/owner/',
        TokenObtainPairView.as_view(
            serializer_class=OwnerTokenObtainPairSerializer),
        name='token_obtain_pair_owner'
    ),
    path(
        'api/token/owner/refresh/',
        TokenRefreshView.as_view(
            serializer_class=OwnerTokenRefreshSerializer),
        name='token_refresh_owner'
    ),
    path(
        'api/token/client/',
        TokenObtainPairView.as_view(
            serializer_class=ClientTokenObtainPairSerializer),
        name='token_obtain_pair_client'
    ),
    path(
        'api/token/client/refresh/',
        TokenRefreshView.as_view(
            serializer_class=ClientTokenRefreshSerializer),
        name='token_refresh_client'
    ),
]
