from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import holidaytrip_viewsets,holidaytripreview_viewsets,holidaytype_viewsets

router = DefaultRouter()

router.register('holiday-trip', holidaytrip_viewsets.HolidayTripViewsets, basename="HolidayTripViewsets")
router.register('holiday-trip-type', holidaytype_viewsets.HolidayTypeViewsets, basename="HolidayTypeViewsets")
router.register('holiday-trip-type-review', holidaytripreview_viewsets.HolidayTripReviewViewsets, basename="HolidayTripReviewViewsets")

urlpatterns = [    
    # path('', include(router.urls)),
]