from rest_framework.routers import DefaultRouter
from ..viewsets.herosection_viewsets import herosectionViewsets

router = DefaultRouter()


router.register('herosection', herosectionViewsets, basename="herosectionViewsets")
