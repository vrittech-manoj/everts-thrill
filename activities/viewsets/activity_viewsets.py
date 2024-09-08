from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Activity
from ..serializers.activity_serializers import ActivityListSerializers, ActivityRetrieveSerializers, ActivityWriteSerializers
from ..utilities.importbase import *
from rest_framework.response import Response
from rest_framework import status

class activityViewsets(viewsets.ModelViewSet):
    serializer_class = ActivityListSerializers
    # permission_classes = [activitiesPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = Activity.objects.all().order_by("-name")

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id','name']
    ordering_fields = ['name']
    ordering = ['name']  # Default ordering

    filterset_fields = {
        'id': ['exact'],
        'name': ['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ActivityWriteSerializers
        elif self.action == 'retrieve':
            return ActivityRetrieveSerializers
        return super().get_serializer_class()
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response(
            {"detail": "Item/s successfully deleted."}, 
            status=status.HTTP_200_OK
        )

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

