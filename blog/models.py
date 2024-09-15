from django.db import models
import uuid
from django.utils.text import slugify
from accounts.models import CustomUser


class Blog(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(CustomUser, related_name="user_blog", on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(upload_to="blog/images", null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=150, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    read_time = models.CharField(max_length=150, default="10 mins")
    is_popular = models.BooleanField(default=False)

    # Meta fields
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.title)}'
        
        # Auto-populate meta fields if not provided
        if not self.meta_title:
            self.meta_title = self.title  
        if not self.meta_description:
            self.meta_description = self.short_description or self.description[:160]  # Default to short description or first 160 chars of description
        if not self.meta_keywords:
            self.meta_keywords = ', '.join(self.title.split())
        
        super(Blog, self).save(*args, **kwargs)
