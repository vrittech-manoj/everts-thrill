from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Review
from ..serializers.review_serializers import ReviewListSerializers, ReviewRetrieveSerializers, ReviewWriteSerializers
from ..utilities.importbase import *

class reviewViewsets(viewsets.ModelViewSet):
    serializer_class = ReviewListSerializers
    permission_classes = [reviewPermission]
    pagination_class = MyPageNumberPagination
    queryset = Review.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id','star_rating']
    ordering_fields = ['id','star_rating']

    filterset_fields = {
        'star_rating': ['exact'],
        'destination': ['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ReviewWriteSerializers
        elif self.action == 'retrieve':
            return ReviewRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

