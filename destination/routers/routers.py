from rest_framework.routers import DefaultRouter
from ..viewsets.destination_viewsets import destinationViewsets

router = DefaultRouter()
auto_api_routers = router


router.register('destination', destinationViewsets, basename="destinationViewsets")
