from django.db import models
from accounts.models import CustomUser
from django.core.exceptions import ValidationError

class Popup(models.Model):
    title = models.CharField(max_length = 200,null = True)
    image = models.ImageField(upload_to='components/popup', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    
    created_date = models.DateField(auto_now_add=True, null = True,blank = True)
    created_date_time = models.DateTimeField(auto_now_add=True, null = True,blank = True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Check if title length exceeds the max_length
        if self.title and len(self.title) > 200:
            raise ValidationError({'title': 'The title cannot exceed 200 characters.'})
        super().save(*args, **kwargs)

class MeetTeam(models.Model):
    member_name = models.CharField(max_length = 200,null = True)
    index = models.PositiveIntegerField(default = 999)
    position = models.CharField(max_length = 200,null = True)
    description = models.TextField()
    image = models.ImageField(upload_to='components/meetteam', null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.member_name}-{self.id}-{self.index}"

class PrivacyPolicy(models.Model):
    description = models.TextField()
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class VisaInformation(models.Model):
    description = models.TextField()
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class TermAndCondition(models.Model):
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
class AboutUs(models.Model):
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class LegalDocuments(models.Model):
    # user = models.ForeignKey(CustomUser,related_name = 'user_legal_documents', on_delete  = models.CASCADE)
    image = models.ImageField(upload_to='components/legal-documents', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class HeroSection(models.Model):
    position = models.CharField(max_length=23, choices=[('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom')],unique=True)
    video = models.FileField(upload_to='hero_section_videos', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
class HeroSectionOverlay(models.Model):
    overlay_text = models.CharField(max_length = 200,null = True,blank=True)
    button_text = models.CharField(max_length = 200,null = True,blank=True)
    button_link = models.URLField(null=True, blank=True)
    is_button = models.BooleanField(default = False)
    is_overlay_text = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
class HeroSectionStats(models.Model):
     stat_text = models.CharField(max_length = 200,null = True,blank=True)
     stat_number = models.CharField(max_length = 200,null = True,blank=True)
     stat_description = models.TextField(null = True,blank=True)
     created_date = models.DateTimeField(auto_now_add=True)
     updated_date = models.DateTimeField(auto_now=True)


class ContacttUsDescription(models.Model):
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
     
    