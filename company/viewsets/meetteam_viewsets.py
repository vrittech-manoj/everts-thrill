from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import MeetTeam
from ..serializers.meetteam_serializers import MeetTeamListSerializers, MeetTeamRetrieveSerializers, MeetTeamWriteSerializers
from ..utilities.importbase import *
from ..utilities.pagination import MyPageNumberPagination
from rest_framework.decorators import action

class meetteamViewsets(viewsets.ModelViewSet):
    serializer_class = MeetTeamListSerializers
    # permission_classes = [companyPermission]
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

    @action(detail=False, methods=['get'], name="dragable", url_path="drag-team")
    def Dragable(self, request, *args, **kwargs):
        target = request.GET.get('target')  # ID of the target object (elephant)
        goal = request.GET.get('goal')  # ID of the goal object (ball)

        from rest_framework.response import Response

        # Fetch the target and goal objects
        try:
            target_obj = MeetTeam.objects.get(id=target)
            goal_obj = MeetTeam.objects.get(id=goal)
        except MeetTeam.DoesNotExist:
            return Response({"error": "Target or Goal object not found"}, status=400)

        target_index = target_obj.index
        goal_index = goal_obj.index

        if target_index < goal_index:
            # Moving target down (target goes after goal)
            affected_objs = MeetTeam.objects.filter(index__gt=target_index, index__lte=goal_index).order_by('index')
            
            # Decrement index of all affected objects
            for obj in affected_objs:
                obj.index -= 1
                obj.save()
            
            # Set target object's new index
            target_obj.index = goal_index
            target_obj.save()

        else:
          # Moving target up (target goes before goal)
            affected_objs = MeetTeam.objects.filter(index__lt=target_index, index__gte=goal_index).order_by('-index')

            # Increment index of all affected objects by 1
            for obj in affected_objs:
                obj.index += 1
                obj.save()

            # Set target object's new index (exact position of the goal)
            target_obj.index = goal_index  # Place the target in the goal's position
            target_obj.save()


        return Response({"status": "success"})
