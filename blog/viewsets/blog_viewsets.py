from rest_framework import viewsets
from ..models import Blog
from ..serializers.blog_serializers import BlogListSerializer, BlogWriteSerializer, BlogRetrieveSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..utilities.permission import AdminViewSetsPermission

class BlogViewSets(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_date')
    permission_classes = [AdminViewSetsPermission]  
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_date', 'title']
    lookup_field = "slug"
    
    filterset_fields = {
        'title': ['exact'],
        'is_popular': ['exact'],
    }

    def get_queryset(self):
        return Blog.objects.all()
    

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
