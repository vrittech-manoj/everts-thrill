from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Review
from ..serializers.review_serializers import ReviewListSerializers, ReviewRetrieveSerializers, ReviewWriteSerializers
from ..utilities.importbase import *

class reviewViewsets(viewsets.ModelViewSet):
    permission_classes = [reviewPermission]
    pagination_class = MyPageNumberPagination

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields =  [ 'id','name', 'star_rating', 'review_type', 'destination__destination_title', 'created_date', 'created_date_time', 'updated_date', ]
    ordering_fields = ['id', 'star_rating','name']
   

    filterset_fields = {
        'star_rating': ['exact'],
        'destination': ['exact'],
        'name': ['exact'],
        'created_date': ['exact','gte','lte'],
    }

    def get_queryset(self):
        user = self.request.user
        if user.is_staff: 
            return Review.objects.all()  
        return Review.visible.all()  


    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ReviewWriteSerializers
        elif self.action == 'retrieve':
            return ReviewRetrieveSerializers
        return ReviewListSerializers

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
