from rest_framework import serializers
from ..models import LegalDocuments

class LegalDocumentsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = LegalDocuments
        fields = '__all__'

class LegalDocumentsRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = LegalDocuments
        fields = '__all__'

class LegalDocumentsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = LegalDocuments
        fields = '__all__'