from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Collection
from ..serializers.collection_serializers import CollectionListSerializers, CollectionRetrieveSerializers, CollectionWriteSerializers
from ..utilities.importbase import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class collectionViewsets(viewsets.ModelViewSet):
    serializer_class = CollectionListSerializers
    # permission_classes = [collectionPermission]
    pagination_class = MyPageNumberPagination
    queryset = Collection.objects.all().order_by("index")

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id','name']
    ordering_fields = ['id','name','index']

    filterset_fields = {
        'id': ['exact'],
        'name':['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CollectionWriteSerializers
        elif self.action == 'retrieve':
            return CollectionRetrieveSerializers
        return super().get_serializer_class()
    
    def create_collection(request):
        serializer = CollectionWriteSerializers(data=request.data)
        if serializer.is_valid():
            collection = serializer.save()
            return Response({"message": "Collection created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response(
            {"detail": "Item/s successfully deleted."}, 
            status=status.HTTP_200_OK
        )


    @action(detail=False, methods=['get'], name="dragableCollection", url_path="drag-collection")
    def Dragable(self, request, *args, **kwargs):
        target = request.GET.get('target')  # ID of the target object 
        goal = request.GET.get('goal')  # ID of the goal object 

        from rest_framework.response import Response

        # Fetch the target and goal objects
        try:
            target_obj = Collection.objects.get(id=target)
            goal_obj = Collection.objects.get(id=goal)
        except Collection.DoesNotExist:
            return Response({"error": "Target or Goal object not found"}, status=400)

        target_index = target_obj.index
        goal_index = goal_obj.index

        if target_index < goal_index:
            # Moving target down (target goes after goal)
            affected_objs = Collection.objects.filter(index__gt=target_index, index__lte=goal_index).order_by('index')
            
            # Decrement index of all affected objects
            for obj in affected_objs:
                obj.index -= 1
                obj.save()
            
            # Set target object's new index
            target_obj.index = goal_index
            target_obj.save()

        else:
          # Moving target up (target goes before goal)
            affected_objs = Collection.objects.filter(index__lt=target_index, index__gte=goal_index).order_by('-index')

            # Increment index of all affected objects by 1
            for obj in affected_objs:
                obj.index += 1
                obj.save()

            # Set target object's new index (exact position of the goal)
            target_obj.index = goal_index  # Place the target in the goal's position
            target_obj.save()


        return Response({"status": "success"})
