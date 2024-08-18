from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import PrivacyPolicy
from ..serializers.privacypolicy_serializers import PrivacyPolicyListSerializers, PrivacyPolicyRetrieveSerializers, PrivacyPolicyWriteSerializers
from ..utilities.importbase import *

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class privacypolicyViewsets(viewsets.ModelViewSet):
    serializer_class = PrivacyPolicyListSerializers
    permission_classes = [companyPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = PrivacyPolicy.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {
    #     'id': ['exact'],
    # }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PrivacyPolicyWriteSerializers
        elif self.action == 'retrieve':
            return PrivacyPolicyRetrieveSerializers
        return super().get_serializer_class()

    @action(detail=False, methods=['post'], name="create-update", url_path="url_path")
    def action_name(self, request, *args, **kwargs):
        description = request.data.get('description', None)
        
        if description is None:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        privacy_policy = PrivacyPolicy.objects.all()
        
        if privacy_policy.exists():
            # Update the existing privacy policy
            privacy_policy = privacy_policy.first()
            privacy_policy.description = description
            privacy_policy.save()
            return Response({"message": "Privacy policy updated successfully."}, status=status.HTTP_200_OK)
        else:
            # Create a new privacy policy
            new_policy = PrivacyPolicy.objects.create(description=description)
            return Response({"message": "Privacy policy created successfully.", "policy_id": new_policy.id}, status=status.HTTP_201_CREATED)
