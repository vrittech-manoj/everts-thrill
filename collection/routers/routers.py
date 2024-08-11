from rest_framework.routers import DefaultRouter
from ..viewsets.collection_viewsets import collectionViewsets

router = DefaultRouter()


router.register('collection-management', collectionViewsets, basename="collectionViewsets")
