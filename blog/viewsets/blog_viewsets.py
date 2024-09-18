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
    queryset = Blog.objects.all().order_by('created_date')
    serializer_class = BlogListSerializer
    permission_classes = [AdminViewSetsPermission] 
    pagination_class = MyPageNumberPagination 
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title','description','short_description','read_time','created_date','created_by']
    # ('public_id', 'user', 'slug', 'title', 'description', 'short_description', 'featured_image', 'created_date', 'created_date_time', 'created_by', 'updated_date', 'read_time', 'is_popular', 'meta_title', 'meta_description', 'meta_keywords', )
    ordering_fields = ['id', 'title', 'created_date']
    lookup_field = "slug"
    
    filterset_fields = {
        'title': ['exact'],
        'is_popular': ['exact'],
        'created_date': ['exact','lte','gte'],
    }

    def get_queryset(self):
            queryset = Blog.objects.all().order_by('-created_date')
            blog_slug = self.request.query_params.get('id')
            # # Filter by is_popular query parameter if provided (e.g. /api/blog-management/?is_popular=true)
            # is_popular = self.request.query_params.get('is_popular')
            # if is_popular:
            #     queryset = queryset.filter(is_popular=is_popular.lower() == 'true')
            
            # Exclude the blog that the user is currently reading if blog_id is provided
            if blog_slug:
                queryset = queryset.exclude(slug=blog_slug)
        
            return queryset
        
        
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

