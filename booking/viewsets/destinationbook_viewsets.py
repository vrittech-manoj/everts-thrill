from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import DestinationBook
from ..serializers.destinationbook_serializers import DestinationBookListSerializers, DestinationBookRetrieveSerializers, DestinationBookWriteSerializers
from ..utilities.importbase import *
from django.shortcuts import get_object_or_404

class destinationbookViewsets(viewsets.ModelViewSet):
    serializer_class = DestinationBookListSerializers
    permission_classes = [bookingPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = DestinationBook.objects.all().order_by("-created_date")
    lookup_field = "slug"

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['full_name', 'email', 'phone_number', 'country', 'airlines', 'number_of_travelers', 'activity', 'package', 'arrival_date', 'departure_date', 'service_type', 'destination', 'customize_trip', 'created_date', 'updated_date',]
    ordering_fields = ['id','full_name']

    filterset_fields = {
        'id': ['exact'],
        'full_name': ['exact'],
        'country': ['exact', 'icontains'],
        'service_type': ['exact', 'icontains'],
        'arrival_date': ['exact','gte','lte'],
        'departure_date': ['exact','gte','lte'],
        'created_date': ['exact','gte','lte'],
        }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DestinationBookWriteSerializers
        elif self.action == 'retrieve':
            return DestinationBookRetrieveSerializers
        return super().get_serializer_class()
    
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(DestinationBook, slug=slug)

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

