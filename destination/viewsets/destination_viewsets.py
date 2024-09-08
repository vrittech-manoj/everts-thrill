from rest_framework import viewsets, permissions, filters
from ..models import Destination
from rest_framework.response import Response
from rest_framework import status

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
from ..utilities.destination_filter import DestinationFilter

class DestinationViewsets(viewsets.ModelViewSet):
    permission_classes = [destinationPermission]
    pagination_class = MyPageNumberPagination
    queryset = Destination.objects.all().order_by("-destination_title")

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['destination_title']
    ordering_fields = ['destination_title', 'id','duration']
    filterset_class = DestinationFilter
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response(
            {"detail": "Item/s successfully deleted."}, 
            status=status.HTTP_200_OK
        )
