from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import holidaytripbook_viewsets,servicebook_viewsets

router = DefaultRouter()

router.register('holiday-trip-book', holidaytripbook_viewsets.HolidayTripBookViewsets, basename="HolidayTripBookViewsets")
router.register('services-book', servicebook_viewsets.ServiceBookBookViewsets, basename="ServiceBookBookViewsets")

urlpatterns = [    
    # path('', include(router.urls)),
]