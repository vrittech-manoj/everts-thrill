from rest_framework.response import Response
from rest_framework import status
from ..models import Queries
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..serializers.queries_serializers import QueriesReadSerializers, QueriesWriteSerializers,QueriesListSerializers
from ..utilities.importbase import *

class QueriesViewsets(viewsets.ModelViewSet):
    serializer_class = QueriesListSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = Queries.objects.all()
    
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    
    filterset_fields = {
        'id': ['exact'],
        'name': ['exact'],
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return QueriesWriteSerializers
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "message": "Query created successfully!",
                "data": serializer.data
            }, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )
