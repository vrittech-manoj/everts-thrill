from ..models import HolidayTripBook
from ..serializers.holidaytripbook_serializers import HolidayTripBookReadSerializers,HolidayTripBookWriteSerializers
from ..utilities.importbase import *

class HolidayTripBookViewsets(viewsets.ModelViewSet):
    serializer_class = HolidayTripBookReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = HolidayTripBook.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return HolidayTripBookWriteSerializers
        return super().get_serializer_class()
    