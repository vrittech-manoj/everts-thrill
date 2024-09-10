from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import HeroSectionOverlay
from ..serializers.herosectionoverlay_serializers import HeroSectionOverlayListSerializers, HeroSectionOverlayRetrieveSerializers, HeroSectionOverlayWriteSerializers
from ..utilities.importbase import *

class herosectionoverlayViewsets(viewsets.ModelViewSet):
    serializer_class = HeroSectionOverlayListSerializers
    permission_classes = [companyPermission]
    pagination_class = MyPageNumberPagination
    queryset = HeroSectionOverlay.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id','overlay_text']
    ordering_fields = ['id','overlay_text']

    filterset_fields = {
        'id': ['exact'],
        'overlay_text': ['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return HeroSectionOverlayWriteSerializers
        elif self.action == 'retrieve':
            return HeroSectionOverlayRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

