from ..models import Testonomial
from ..serializers.testonomial_serializers import TestonomialReadSerializers,TestonomialWriteSerializers
from ..utilities.importbase import *

class TestonomialViewsets(viewsets.ModelViewSet):
    serializer_class = TestonomialReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Testonomial.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return TestonomialWriteSerializers
        return super().get_serializer_class()
    