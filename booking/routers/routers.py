from rest_framework.routers import DefaultRouter
from ..viewsets.destinationbook_viewsets import destinationbookViewsets
from ..viewsets.servicebook_viewsets import servicebookViewsets

router = DefaultRouter()


router.register('destinationbook', destinationbookViewsets, basename="destinationbookViewsets")
router.register('servicebook', servicebookViewsets, basename="servicebookViewsets")
