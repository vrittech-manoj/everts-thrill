from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import TermAndCondition
from ..serializers.termandcondition_serializers import TermAndConditionListSerializers, TermAndConditionRetrieveSerializers, TermAndConditionWriteSerializers
from ..utilities.importbase import *

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class termandconditionViewsets(viewsets.ModelViewSet):
    serializer_class = TermAndConditionListSerializers
    permission_classes = [companyPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = TermAndCondition.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TermAndConditionWriteSerializers
        elif self.action == 'retrieve':
            return TermAndConditionRetrieveSerializers
        return super().get_serializer_class()

    @action(detail=False, methods=['post'], name="create-update", url_path="url_path")
    def action_name(self, request, *args, **kwargs):
        description = request.data.get('description', None)
        
        if description is None:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        term_and_condition = TermAndCondition.objects.all()
        
        if term_and_condition.exists():
            # Update the existing term and condition
            term_and_condition = term_and_condition.first()
            term_and_condition.description = description
            term_and_condition.save()
            return Response({"message": "Terms and conditions updated successfully."}, status=status.HTTP_200_OK)
        else:
            # Create a new term and condition
            new_term_and_condition = TermAndCondition.objects.create(description=description)
            return Response({"message": "Terms and conditions created successfully.", "id": new_term_and_condition.id}, status=status.HTTP_201_CREATED)
