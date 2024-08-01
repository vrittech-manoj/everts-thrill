from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import testonomial_viewsets

router = DefaultRouter()

router.register('testonomials', testonomial_viewsets.TestonomialViewsets, basename="TestonomialViewsets")

urlpatterns = [    
    # path('', include(router.urls)),
]