from django.urls import path,include
from .export import GetSampleAPIView

urlpatterns = [
    path('export-sample/<str:type>/',GetSampleAPIView.as_view(),name='get-sample')
]