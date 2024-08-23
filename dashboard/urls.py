from django.urls import path
from .views import GetDashboardAPIView

urlpatterns=[
    path('dashboard/',GetDashboardAPIView.as_view(),name="get-dashboard"),
]