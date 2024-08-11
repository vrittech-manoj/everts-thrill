from rest_framework.routers import DefaultRouter
from ..viewsets.airlines_viewsets import airlinesViewsets

router = DefaultRouter()
auto_api_routers = router


router.register('airlines', airlinesViewsets, basename="airlinesViewsets")
