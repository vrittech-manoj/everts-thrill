from ..models import Queries
from ..serializers.queries_serializers import QueriesReadSerializers,QueriesWriteSerializers
from ..utilities.importbase import *

class QueriesViewsets(viewsets.ModelViewSet):
    serializer_class = QueriesReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Queries.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return QueriesWriteSerializers
        return super().get_serializer_class()
    