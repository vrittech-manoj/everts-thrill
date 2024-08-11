from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import DestinationGalleryImages
from ..utilities.permissions import destinationPermission
from ..serializers.destinationgalleryimages_serializers import DestinationGalleryImagesListSerializers, DestinationGalleryImagesRetrieveSerializers, DestinationGalleryImagesWriteSerializers
from ..utilities.importbase import *

class destinationgalleryimagesViewsets(viewsets.ModelViewSet):
    serializer_class = DestinationGalleryImagesListSerializers
    permission_classes = [destinationPermission]
    authentication_classes = [JWTAuthentication]
    # pagination_class = MyPageNumberPagination
    queryset = DestinationGalleryImages.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {
    #     'id': ['exact'],
    # }

    def get_queryset(self):
        queryset = super().get_queryset()
        #return queryset.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DestinationGalleryImagesWriteSerializers
        elif self.action == 'retrieve':
            return DestinationGalleryImagesRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

