from rest_framework.routers import DefaultRouter
from ..viewsets.popup_viewsets import popupViewsets
from ..viewsets.legaldocuments_viewsets import legaldocumentsViewsets
from ..viewsets.termandcondition_viewsets import termandconditionViewsets
from ..viewsets.visainformation_viewsets import visainformationViewsets
from ..viewsets.privacypolicy_viewsets import privacypolicyViewsets
from ..viewsets.meetteam_viewsets import meetteamViewsets

router = DefaultRouter()
auto_api_routers = router


router.register('popup', popupViewsets, basename="popupViewsets")
router.register('meetteam', meetteamViewsets, basename="meetteamViewsets")
router.register('privacypolicy', privacypolicyViewsets, basename="privacypolicyViewsets")
router.register('visainformation', visainformationViewsets, basename="visainformationViewsets")
router.register('termandcondition', termandconditionViewsets, basename="termandconditionViewsets")
router.register('legaldocuments', legaldocumentsViewsets, basename="legaldocumentsViewsets")
