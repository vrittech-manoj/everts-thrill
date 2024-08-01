from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import queries_viewsets

router = DefaultRouter()

router.register('queries', queries_viewsets.QueriesViewsets, basename="queriesviewsets")

urlpatterns = [    
    # path('', include(router.urls)),
]