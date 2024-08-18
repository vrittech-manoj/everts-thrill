from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Departure
from ..serializers.departure_serializers import DepartureListSerializers, DepartureRetrieveSerializers, DepartureWriteSerializers
from ..utilities.importbase import *

class departureViewsets(viewsets.ModelViewSet):
    serializer_class = DepartureListSerializers
    permission_classes = [departurePermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = Departure.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        #return queryset.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DepartureWriteSerializers
        elif self.action == 'retrieve':
            return DepartureRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

