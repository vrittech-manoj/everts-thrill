from rest_framework import viewsets, permissions, filters
from ..models import Destination

from django.shortcuts import get_object_or_404
from ..serializers.destination_serializers import (
    DestinationlistUserSerializers,
    DestinationlistAdminSerializers,
    DestinationRetrieveUserSerializers,
    DestinationRetrieveAdminSerializers,
    DestinationWriteSerializers
    

)
from ..utilities.importbase import *
from ..utilities.permissions import destinationPermission
from accounts import roles
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters

# Custom filter set for Destination model
class DestinationFilter(django_filters.FilterSet):
    package_id = django_filters.CharFilter(field_name='packages__id', lookup_expr='exact')

    class Meta:
        model = Destination
        fields = {
            'destination_title': ['exact', 'icontains'],
            'nature_of_trip': ['exact', 'icontains'],
            'activities': ['exact'],
            # 'package_name' is already defined as a custom filter above
        }

class DestinationViewsets(viewsets.ModelViewSet):
    permission_classes = [destinationPermission]
    pagination_class = MyPageNumberPagination
    queryset = Destination.objects.all().order_by("-destination_title")

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['destination_title']
    ordering_fields = ['destination_title', 'id']
    filterset_class = DestinationFilter  # Use the custom filter set here
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DestinationWriteSerializers
        elif self.action == "list":
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN, roles.SUPER_ADMIN]:
                return DestinationlistAdminSerializers
            else:
                return DestinationlistUserSerializers
        elif self.action == "retrieve":
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN, roles.SUPER_ADMIN]:
                return DestinationRetrieveAdminSerializers
            else:
                return DestinationRetrieveUserSerializers
        return super().get_serializer_class()
    
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Destination, slug=slug)
