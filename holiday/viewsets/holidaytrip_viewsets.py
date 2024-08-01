from ..models import HolidayTrip
from ..serializers.holiday_trip_serializers import (
    HolidayTriplistUserSerializers,HolidayTriplistAdminSerializers,HolidayTripRetrieveUserSerializers,HolidayTripRetrieveAdminSerializers,
    HolidayTripWriteSerializers
)
from ..utilities.importbase import *
from accounts import roles

class HolidayTripViewsets(viewsets.ModelViewSet):
    serializer_class = HolidayTriplistUserSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = HolidayTrip.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return HolidayTripWriteSerializers
        
        elif self.action == "list":
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN]:
                return HolidayTriplistAdminSerializers
            else:
                return HolidayTriplistUserSerializers
            
        elif self.action == "retrieve":
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN]:
                return HolidayTripRetrieveAdminSerializers
            else:
                return HolidayTripRetrieveUserSerializers
        

        return super().get_serializer_class()
    