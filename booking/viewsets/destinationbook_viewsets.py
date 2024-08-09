from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import DestinationBook
from ..serializers.destinationbook_serializers import DestinationBookListSerializers, DestinationBookRetrieveSerializers, DestinationBookWriteSerializers
from ..utilities.importbase import *

class destinationbookViewsets(viewsets.ModelViewSet):
    serializer_class = DestinationBookListSerializers
    # permission_classes = [bookingPermission]
    # authentication_classes = [JWTAuthentication]
    #pagination_class = MyPageNumberPagination
    queryset = DestinationBook.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {
    #     'id': ['exact'],
    # }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DestinationBookWriteSerializers
        elif self.action == 'retrieve':
            return DestinationBookRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

