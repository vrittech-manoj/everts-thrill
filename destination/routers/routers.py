from rest_framework.routers import DefaultRouter
from ..viewsets.package_viewsets import PackageViewsets
from ..viewsets.destinationreview_viewsets import DestinationReviewViewsets
from ..viewsets.destinationgalleryimages_viewsets import destinationgalleryimagesViewsets
from ..viewsets.destination_viewsets import DestinationViewsets

router = DefaultRouter()
auto_api_routers = router


router.register('package', PackageViewsets, basename="packageViewsets")
router.register('destination', DestinationViewsets, basename="destinationViewsets")
router.register('destinationgalleryimages', destinationgalleryimagesViewsets, basename="destinationgalleryimagesViewsets")
router.register('destinationreview', DestinationReviewViewsets, basename="destinationreviewViewsets")
