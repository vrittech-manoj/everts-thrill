from django.db import models
from accounts.models import CustomUser

class Popup(models.Model):
    title = models.CharField(max_length = 200,null = True)
    image = models.ImageField(upload_to='components/popup', null=True, blank=True)
    url = models.URLField(null=True, blank=True)

class MeetTeam(models.Model):
    member_name = models.CharField(max_length = 200,null = True)
    position = models.CharField(max_length = 200,null = True)
    description = models.TextField()
    image = models.ImageField(upload_to='components/popup', null=True, blank=True)
    url = models.URLField(null=True, blank=True)

class PrivacyPolicy(models.Model):
    description = models.TextField()

class VisaInformation(models.Model):
    description = models.TextField()

class TermAndCondition(models.Model):
    description = models.TextField()

class LegalDocuments(models.Model):
    user = models.ForeignKey(CustomUser,related_name = 'user_legal_documents', on_delete  = models.CASCADE)
    image = models.ImageField(upload_to='components/popup', null=True, blank=True)
    url = models.URLField(null=True, blank=True)

class HeroSection(models.Model):
    position = models.CharField(max_length = 23,choices = (('top','Top'),('middle','Middle'),('bottom','Bottom')))
    video = models.FileField(upload_to='hero_section_videos', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Hero Section Video: {self.video}"