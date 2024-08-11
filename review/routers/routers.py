from rest_framework.routers import DefaultRouter
from ..viewsets.review_viewsets import reviewViewsets

router = DefaultRouter()

router.register('review', reviewViewsets, basename="reviewViewsets")
