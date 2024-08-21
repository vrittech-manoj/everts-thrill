from rest_framework import serializers
from ..models import LegalDocuments
from accounts.models import CustomUser

class CustomUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name =  "account_legaldocuments"
        model = CustomUser
        # fields = '__all__' 
        exclude = ['password']
        
class LegalDocumentsListSerializers(serializers.ModelSerializer):
    # user_legal_documents = CustomUserReadSerializer(read_only = True)
    class Meta:
        model = LegalDocuments
        fields = '__all__'

class LegalDocumentsRetrieveSerializers(serializers.ModelSerializer):
    # user_legal_documents = CustomUserReadSerializer(read_only = True)
    class Meta:
        model = LegalDocuments
        fields = '__all__'

class LegalDocumentsWriteSerializers(serializers.ModelSerializer):
    # user_legal_documents = CustomUserReadSerializer()
    class Meta:
        model = LegalDocuments
        fields = '__all__'