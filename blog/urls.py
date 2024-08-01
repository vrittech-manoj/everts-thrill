from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import blog_viewsets

router = DefaultRouter()

router.register('blogs', blog_viewsets.BlogViewSets, basename="BlogViewSets")

urlpatterns = [    
    # path('', include(router.urls)),
]