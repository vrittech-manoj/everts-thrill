from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import destination_viewsets, destinationreview_viewsets, package_viewsets

router = DefaultRouter()

router.register(r'destination/(?P<slug>[\w-]+)', destination_viewsets.DestinationViewsets, basename="DestinationViewsets")
router.register('package', package_viewsets.PackageViewsets, basename="PackageViewsets")
router.register('package-review', destinationreview_viewsets.DestinationReviewViewsets, basename="DestinationReviewViewsets")

urlpatterns = [
    # path('', include(router.urls)), 
]