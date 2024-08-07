from rest_framework.routers import DefaultRouter
from ..viewsets.collection_viewsets import collectionViewsets

router = DefaultRouter()
auto_api_routers = router


router.register('collection', collectionViewsets, basename="collectionViewsets")
