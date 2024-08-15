from ..models import DestinationReview
from ..serializers.destination_review_serializers import DestinationReviewReadSerializers,DestinationReviewWriteSerializers
from ..utilities.importbase import *
from ..utilities.permissions import destinationPermission


class DestinationReviewViewsets(viewsets.ModelViewSet):
    serializer_class = DestinationReviewReadSerializers
    permission_classes = [destinationPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = DestinationReview.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['user']
    ordering_fields = ['id']
    filterset_fields = {
        'stars': ['exact'],
    }

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return DestinationReviewWriteSerializers
        return super().get_serializer_class()
    