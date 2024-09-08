from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Collection
from ..serializers.collection_serializers import CollectionListSerializers, CollectionRetrieveSerializers, CollectionWriteSerializers
from ..utilities.importbase import *

class collectionViewsets(viewsets.ModelViewSet):
    serializer_class = CollectionListSerializers
    permission_classes = [collectionPermission]
    pagination_class = MyPageNumberPagination
    queryset = Collection.objects.all().order_by("-name")

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id','name']
    ordering_fields = ['id','name','index']

    filterset_fields = {
        'id': ['exact'],
        'name':['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CollectionWriteSerializers
        elif self.action == 'retrieve':
            return CollectionRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

