from django.db import models

# Create your models here.   
class HeroSection(models.Model):
    position = models.CharField(max_length = 23,choices = (('top','Top'),('middle','Middle'),('bottom','Bottom')))
    video = models.FileField(upload_to='hero_section_videos', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Hero Section Video: {self.video}"