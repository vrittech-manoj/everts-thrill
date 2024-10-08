from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Faqs
from ..serializers.faqs_serializers import FaqsListSerializers, FaqsRetrieveSerializers, FaqsWriteSerializers
from ..utilities.importbase import *

class faqsViewsets(viewsets.ModelViewSet):
    serializer_class = FaqsListSerializers
    permission_classes = [faqsPermission]
    pagination_class = MyPageNumberPagination
    queryset = Faqs.objects.all().order_by("created_date_time")

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id']

    filterset_fields = {
        'title': ['exact'],
        'destination': ['exact'],
        'faq_type': ['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return FaqsWriteSerializers
        elif self.action == 'retrieve':
            return FaqsRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

