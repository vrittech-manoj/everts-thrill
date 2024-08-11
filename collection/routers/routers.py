from rest_framework.routers import DefaultRouter
from ..viewsets.collection_viewsets import collectionViewsets

router = DefaultRouter()


router.register('collection', collectionViewsets, basename="collectionViewsets")
