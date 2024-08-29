from ..models import Blog
from ..serializers.blog_serializers import BlogListSerializers, BlogWriteSerializers, BlogRetrieveSerializers
from ..utilities.importbase import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class BlogViewSets(viewsets.ModelViewSet):
    serializer_class = BlogListSerializers
    permission_classes = [AdminViewSetsPermission]
    pagination_class = MyPageNumberPagination
    queryset = Blog.objects.all().order_by("created_date")
    
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'title','created_date']

    filterset_fields = {
        'title': ['exact'],
        'is_popular': ['exact'],
    }
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BlogWriteSerializers
        elif self.action == 'retrieve':
            return BlogRetrieveSerializers
        return super().get_serializer_class()
