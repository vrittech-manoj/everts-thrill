from django.contrib import admin
from .models import Popup, MeetTeam, TermAndCondition, VisaInformation, LegalDocuments

# Register your models here.
admin.site.register(Popup)
admin.site.register(MeetTeam)
admin.site.register(TermAndCondition)
admin.site.register(VisaInformation)
admin.site.register(LegalDocuments)