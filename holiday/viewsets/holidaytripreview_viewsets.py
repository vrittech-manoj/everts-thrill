from ..models import HolidayTripReview
from ..serializers.holiday_trip_review_serializers import HolidayTripReviewReadSerializers,HolidayTripReviewWriteSerializers
from ..utilities.importbase import *

class HolidayTripReviewViewsets(viewsets.ModelViewSet):
    serializer_class = HolidayTripReviewReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = HolidayTripReview.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return HolidayTripReviewWriteSerializers
        return super().get_serializer_class()
    