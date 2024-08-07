from rest_framework.routers import DefaultRouter
from ..viewsets.holidaytype_viewsets import HolidayTypeViewsets
from ..viewsets.holidaytripreview_viewsets import HolidayTripReviewViewsets
from ..viewsets.holidaytripgalleryimages_viewsets import holidaytripgalleryimagesViewsets
from ..viewsets.holidaytrip_viewsets import HolidayTripViewsets

router = DefaultRouter()
auto_api_routers = router


router.register('holidaytype', HolidayTypeViewsets, basename="holidaytypeViewsets")
router.register('holidaytrip', HolidayTripViewsets, basename="holidaytripViewsets")
router.register('holidaytripgalleryimages', holidaytripgalleryimagesViewsets, basename="holidaytripgalleryimagesViewsets")
router.register('holidaytripreview', HolidayTripReviewViewsets, basename="holidaytripreviewViewsets")
