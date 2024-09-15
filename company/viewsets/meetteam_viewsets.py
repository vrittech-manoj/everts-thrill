from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import MeetTeam
from ..serializers.meetteam_serializers import MeetTeamListSerializers, MeetTeamRetrieveSerializers, MeetTeamWriteSerializers
from ..utilities.importbase import *

class meetteamViewsets(viewsets.ModelViewSet):
    serializer_class = MeetTeamListSerializers
    permission_classes = [companyPermission]
    pagination_class = MyPageNumberPagination
    queryset = MeetTeam.objects.all().order_by("index")

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id','member_name','position']
    ordering_fields = ['id','member_name','position','index']

    filterset_fields = {
        'id': ['exact'],
        'member_name': ['exact'],
        'position': ['exact'],
        'index': ['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MeetTeamWriteSerializers
        elif self.action == 'retrieve':
            return MeetTeamRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

