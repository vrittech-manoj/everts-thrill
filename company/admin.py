from django.contrib import admin
from .models import Popup, MeetTeam, TermAndCondition, VisaInformation,AboutUs, LegalDocuments,HeroSection,PrivacyPolicy,HeroSectionOverlay

# Register your models here.
admin.site.register(Popup)
admin.site.register(MeetTeam)
admin.site.register(TermAndCondition)
admin.site.register(VisaInformation)
admin.site.register(LegalDocuments)
admin.site.register(HeroSection)
admin.site.register(PrivacyPolicy)
admin.site.register(HeroSectionOverlay)
admin.site.register(AboutUs)