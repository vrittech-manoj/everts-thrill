from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Airlines
from ..serializers.airlines_serializers import AirlinesListSerializers, AirlinesRetrieveSerializers, AirlinesWriteSerializers
from ..utilities.importbase import *

class airlinesViewsets(viewsets.ModelViewSet):
    serializer_class = AirlinesListSerializers
    permission_classes = [airlinesPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = Airlines.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id','name']

    filterset_fields = {
        'id': ['exact'],
        'name':['exact']
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AirlinesWriteSerializers
        elif self.action == 'retrieve':
            return AirlinesRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

