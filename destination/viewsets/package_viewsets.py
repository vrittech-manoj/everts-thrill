from ..models import Package
from ..serializers.destination_type_serializers import PackageReadSerializers,PackageWriteSerializers
from ..utilities.importbase import *
from rest_framework.permissions import IsAuthenticated
from accounts import roles

class PackageViewsets(viewsets.ModelViewSet):
    serializer_class = PackageReadSerializers
    permission_classes = [destinationPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Package.objects.all().order_by("-id")

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id','name']
    filterset_fields = {
        'name': ['exact', 'icontains'],
    }

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return PackageWriteSerializers
        elif self.action in ['list','retrieve']:
            return super().get_serializer_class()
    