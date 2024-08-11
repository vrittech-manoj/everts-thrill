from rest_framework.routers import DefaultRouter
from ..viewsets.departure_viewsets import departureViewsets

router = DefaultRouter()
auto_api_routers = router


router.register('departure', departureViewsets, basename="departureViewsets")
