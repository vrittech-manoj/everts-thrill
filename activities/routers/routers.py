from rest_framework.routers import DefaultRouter
from ..viewsets.activity_viewsets import activityViewsets

router = DefaultRouter()
auto_api_routers = router


router.register('activity-management', activityViewsets, basename="activityViewsets")
