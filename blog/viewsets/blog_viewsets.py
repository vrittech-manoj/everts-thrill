from ..models import Blog
from ..serializers.blog_serializers import BlogListSerializers, BlogWriteSerializers, BlogRetrieveSerializers
from ..utilities.importbase import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

class BlogViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    pagination_class = MyPageNumberPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'title', 'created_date']
    queryset = Blog.objects.all().order_by("created_date") 

    filterset_fields = {
        'title': ['exact'],
        'is_popular': ['exact'],
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BlogWriteSerializers
        elif self.action == 'retrieve':
            return BlogRetrieveSerializers
        return BlogListSerializers  #

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
