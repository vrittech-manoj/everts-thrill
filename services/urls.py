from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import services_viewsets

router = DefaultRouter()

router.register('services', services_viewsets.ServicesViewsets, basename="ServicesViewsets")

urlpatterns = [    
    # path('', include(router.urls)),
]