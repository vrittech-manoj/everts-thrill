from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Popup
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
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
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error': e.message_dict}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        try:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except ValidationError as e:
            return Response({'error': e.message_dict}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, partial=True)