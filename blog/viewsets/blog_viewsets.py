from ..models import Blog
from ..serializers.blog_serializers import BlogListSerializers, BlogWriteSerializers, BlogRetrieveSerializers
from ..utilities.importbase import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

class BlogViewSets(viewsets.ModelViewSet):
    permission_classes = [AdminViewSetsPermission] 
    pagination_class = MyPageNumberPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'title', 'created_date']
    
    filterset_fields = {
        'title': ['exact'],
        'is_popular': ['exact'],
    }

    def get_queryset(self):
        queryset = Blog.objects.all().order_by("created_date")
        
        # Check if 'is_popular' filter is present in the query parameters
        is_popular_filter = self.request.query_params.get('is_popular')
        
        if is_popular_filter is not None:
            # Filter the queryset to only include popular blogs
            queryset = queryset.filter(is_popular=True)
        
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BlogWriteSerializers
        elif self.action == 'retrieve':
            return BlogRetrieveSerializers
        return BlogListSerializers  # Default serializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user.username)
