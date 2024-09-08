from rest_framework.routers import DefaultRouter
from ..viewsets.destinationbook_viewsets import destinationbookViewsets
from ..viewsets.servicebook_viewsets import servicebookViewsets

router = DefaultRouter()


router.register('booking-management', destinationbookViewsets, basename="destinationbookViewsets")
# router.register('booking-service', servicebookViewsets, basename="servicebookViewsets")
