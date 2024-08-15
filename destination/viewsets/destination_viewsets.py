from rest_framework import viewsets, permissions, filters
from ..models import Destination
from ..serializers.destination_serializers import (
    DestinationlistUserSerializers,
    DestinationlistAdminSerializers,
    DestinationRetrieveUserSerializers,
    DestinationRetrieveAdminSerializers,
    DestinationWriteSerializers
)
from ..utilities.importbase import *
from accounts import roles
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class DestinationViewsets(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [destinationPermission]
    pagination_class = MyPageNumberPagination
    queryset = Destination.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['destination_title']
    ordering_fields = ['title', 'id']
    filterset_fields = {
        'destination_title': ['exact', 'icontains'],
        'nature_of_trip': ['exact', 'icontains'],
    }
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
