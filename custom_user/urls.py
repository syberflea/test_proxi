from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, ClientViewSet, ClientAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .jwt_views import login_view


router = DefaultRouter()

router.register('owner', OwnerViewSet)
router.register('client', ClientViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('client_post/', ClientAPIView.as_view())
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/login/', login_view, name='login'),
]
