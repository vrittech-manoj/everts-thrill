from ..models import ServiceBook
from ..serializers.servicebook_serializers import ServiceBookReadSerializers,ServiceBookWriteSerializers
from ..utilities.importbase import *

class ServiceBookBookViewsets(viewsets.ModelViewSet):
    serializer_class = ServiceBookReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = ServiceBook.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return ServiceBookWriteSerializers
        return super().get_serializer_class()
    