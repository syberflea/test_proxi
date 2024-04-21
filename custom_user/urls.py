from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, ClientViewSet, ClientAPIView, CreateClientViewSet, RetrieveClientViewSet, UpdateClientViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .jwt_views import login_view


router = DefaultRouter()


router.register(r'client/create',
                CreateClientViewSet,
                basename='create_client')
router.register(r'client/get_profile',
                RetrieveClientViewSet,
                basename='get_client_profile')
router.register(r'client/edit_profile',
                UpdateClientViewSet,
                basename='edit_client_profile')
# router.register(r'client/get_JWT',)
# router.register(r'client/refresh_JWT',)


urlpatterns = [
    path('', include(router.urls)),
    # path('client_post/', ClientAPIView.as_view())
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/login/', login_view, name='login'),
]
