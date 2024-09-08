from rest_framework import viewsets
from ..models import Blog
from ..serializers.blog_serializers import BlogListSerializer, BlogWriteSerializer, BlogRetrieveSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..utilities.permission import AdminViewSetsPermission
from ..utilities.pagination import *
from rest_framework.response import Response
from rest_framework import status

class BlogViewSets(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_date')
    permission_classes = [AdminViewSetsPermission] 
    pagination_class = MyPageNumberPagination 
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'title', 'created_date']
    lookup_field = "slug"
    
    filterset_fields = {
        'title': ['exact'],
        'is_popular': ['exact'],
    }

    def get_queryset(self):
        return Blog.objects
    

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BlogWriteSerializer
        elif self.action == 'retrieve':
            return BlogRetrieveSerializer
        return BlogListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response(
            {"detail": "Item/s successfully deleted."}, 
            status=status.HTTP_200_OK
        )

