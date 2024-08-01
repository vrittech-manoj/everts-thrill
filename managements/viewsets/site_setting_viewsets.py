from ..models import SiteSetting
from ..serializers.site_settings_serializer import SiteSettingReadSerializers,SiteSettingWriteSerializers
from ..utilities.importbase import *

class SiteSettingViewsets(viewsets.ModelViewSet):
    serializer_class = SiteSettingReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = SiteSetting.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return SiteSettingWriteSerializers
        return super().get_serializer_class()
    