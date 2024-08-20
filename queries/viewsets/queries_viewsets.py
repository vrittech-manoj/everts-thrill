from ..models import Queries
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..serializers.queries_serializers import QueriesReadSerializers,QueriesWriteSerializers
from ..utilities.importbase import *

class QueriesViewsets(viewsets.ModelViewSet):
    serializer_class = QueriesReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Queries.objects.all()
    
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['user__first_name']
    ordering_fields = ['id','user__first_name']

    filterset_fields = {
        'id': ['exact'],
        'user__first_name':['exact'],
    }
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return QueriesWriteSerializers
        return super().get_serializer_class()
    