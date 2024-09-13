from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import HeroSectionStats
from ..serializers.herosectionstats_serializers import HeroSectionStatsListSerializers, HeroSectionStatsRetrieveSerializers, HeroSectionStatsWriteSerializers
from ..utilities.importbase import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class herosectionstatsViewsets(viewsets.ModelViewSet):
    serializer_class = HeroSectionStatsListSerializers
    permission_classes = [companyPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = HeroSectionStats.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    filterset_fields = {
        'id': ['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return HeroSectionStatsWriteSerializers
        elif self.action == 'retrieve':
            return HeroSectionStatsRetrieveSerializers
        return super().get_serializer_class()
    def create(self, request, *args, **kwargs):
        data = request.data['stats']
        
        # Check if the request data is a list (indicating multiple objects)
        if isinstance(data, list):
            for item in data:
                if 'id' in item:
                    instance = self.get_queryset().filter(id=item['id']).first()
                    if instance:
                        serializer = self.get_serializer(instance, data=item, partial=True)
                    else:
                        serializer = self.get_serializer(data=item)
                else:
                    serializer = self.get_serializer(data=item)

                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                
        else:
            if 'id' in data:
                instance = self.get_queryset().filter(id=data['id']).first()
                if instance:
                    serializer = self.get_serializer(instance, data=data, partial=True)
                else:
                    serializer = self.get_serializer(data=data)
            else:
                serializer = self.get_serializer(data=data)

            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    