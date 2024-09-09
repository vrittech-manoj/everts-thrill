from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Departure
from ..serializers.departure_serializers import DepartureListSerializers, DepartureRetrieveSerializers, DepartureWriteSerializers
from ..utilities.importbase import *
from ..utilities.departure_filter import DepartureFilter 

class departureViewsets(viewsets.ModelViewSet):
    serializer_class = DepartureListSerializers
    permission_classes = [departurePermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = Departure.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'name', 'index']
    
    filterset_class = DepartureFilter

    def get_queryset(self):
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DepartureWriteSerializers
        elif self.action == 'retrieve':
            return DepartureRetrieveSerializers
        return super().get_serializer_class()
