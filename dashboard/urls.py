from django.urls import path
from .views import GetDashboardAPIView

urlpatterns=[
    path('dashboard-view/<str:type>/',GetDashboardAPIView.as_view(),name="get-dashboard"),
]