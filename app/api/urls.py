from rest_framework import routers
from django.urls import path, include
from .views import PhotoViewSet

router = routers.DefaultRouter()

router.register('photos', PhotoViewSet, basename="photos")

urlpatterns = [
    path("v1/", include(router.urls)),
]