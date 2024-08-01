from ..models import Blog
from ..serializers.blog_serializers import BlogReadSerializers,BlogWriteSerializers
from ..utilities.importbase import *

class BlogViewSets(viewsets.ModelViewSet):
    serializer_class = BlogReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Blog.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return BlogWriteSerializers
        return super().get_serializer_class()
    