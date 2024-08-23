from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import HeroSection
from ..serializers.herosection_serializers import (
    HeroSectionListSerializers, 
    HeroSectionRetrieveSerializers, 
    HeroSectionWriteSerializers
)
from ..utilities.importbase import companyPermission, JWTAuthentication, MyPageNumberPagination

class herosectionViewsets(viewsets.ModelViewSet):
    serializer_class = HeroSectionListSerializers
    permission_classes = [companyPermission]
    pagination_class = MyPageNumberPagination
    queryset = HeroSection.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return HeroSectionWriteSerializers
        elif self.action == 'retrieve':
            return HeroSectionRetrieveSerializers
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        position = request.data.get('position')

        # Use update_or_create to either update the existing entry or create a new one
        instance, created = HeroSection.objects.update_or_create(
            position=position,
            defaults={
                'video': request.data.get('video'),
                'video_link': request.data.get('video_link')
            }
        )

        # Serialize the instance and return the response
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Update or create the instance
        instance, created = HeroSection.objects.update_or_create(
            position=request.data.get('position', instance.position),
            defaults={
                'video': request.data.get('video', instance.video),
                'video_link': request.data.get('video_link', instance.video_link)
            }
        )

        # Serialize the updated instance
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

