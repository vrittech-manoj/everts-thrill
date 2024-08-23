from django.urls import path,include
from .export import getSample

urlpatterns = [
    path('export-sample/<str:type>/',getSample.as_view()),
]