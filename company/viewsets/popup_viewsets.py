from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Popup
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers.popup_serializers import PopupListSerializers, PopupRetrieveSerializers, PopupWriteSerializers

class popupViewsets(viewsets.ModelViewSet):
    serializer_class = PopupListSerializers
    queryset = Popup.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PopupWriteSerializers
        elif self.action == 'retrieve':
            return PopupRetrieveSerializers
        return super().get_serializer_class()