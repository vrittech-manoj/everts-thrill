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
        # Check if the request data is a list (indicating multiple objects)
        data = request.data['stats']
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        # Check if the request data is a list (indicating multiple objects)
        data = request.data['stats']
        
        if isinstance(data, list):
            # For bulk update, each item should have an ID
            for item in data:
                if 'id' not in item:
                    return Response({"detail": "ID is required for each object in bulk update"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Retrieve the queryset of the objects to update
            partial = kwargs.pop('partial', False)
            instance_ids = [item['id'] for item in data]
            instances = self.get_queryset().filter(id__in=instance_ids)

            if len(instances) != len(data):
                return Response({"detail": "Some objects do not exist"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(instances, data=data, many=True, partial=partial)
        else:
            # Single update: ID must be provided
            if 'id' not in data:
                return Response({"detail": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
            
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=data, partial=kwargs.get('partial', False))

        # Validate and perform the update
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
