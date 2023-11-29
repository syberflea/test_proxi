from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, ClientViewSet


router = DefaultRouter()

router.register('owner', OwnerViewSet)
router.register('client', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
