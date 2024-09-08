from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import site_setting_viewsets

router = DefaultRouter()

# router.register('site-setting', site_setting_viewsets.SiteSettingViewsets, basename="SiteSettingViewsets")

urlpatterns = [    
    # path('', include(router.urls)),
]