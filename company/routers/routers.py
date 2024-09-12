from rest_framework.routers import DefaultRouter
from ..viewsets.popup_viewsets import popupViewsets
from ..viewsets.herosectionstats_viewsets import herosectionstatsViewsets
from ..viewsets.aboutus_viewsets import aboutusViewsets
from ..viewsets.herosectionoverlay_viewsets import herosectionoverlayViewsets
from ..viewsets.herosection_viewsets import herosectionViewsets
from ..viewsets.legaldocuments_viewsets import legaldocumentsViewsets
from ..viewsets.termandcondition_viewsets import termandconditionViewsets
from ..viewsets.visainformation_viewsets import visainformationViewsets
from ..viewsets.privacypolicy_viewsets import privacypolicyViewsets
from ..viewsets.meetteam_viewsets import meetteamViewsets

router = DefaultRouter()    


router.register('popup', popupViewsets, basename="popupViewsets")
router.register('meetteam', meetteamViewsets, basename="meetteamViewsets")
router.register('privacypolicy', privacypolicyViewsets, basename="privacypolicyViewsets")
router.register('visainformation', visainformationViewsets, basename="visainformationViewsets")
router.register('termandcondition', termandconditionViewsets, basename="termandconditionViewsets")
router.register('legaldocuments', legaldocumentsViewsets, basename="legaldocumentsViewsets")
router.register('hero-section', herosectionViewsets, basename="herosectionViewsets")
router.register('herosectionoverlay', herosectionoverlayViewsets, basename="herosectionoverlayViewsets")
router.register('aboutus', aboutusViewsets, basename="aboutusViewsets")
router.register('herosectionstats', herosectionstatsViewsets, basename="herosectionstatsViewsets")
