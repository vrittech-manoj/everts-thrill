from rest_framework import serializers
from ..models import MeetTeam

class MeetTeamListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeetTeam
        fields = '__all__'

class MeetTeamRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeetTeam
        fields = '__all__'

class MeetTeamWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeetTeam
        fields = '__all__'
    
    def validate(self, data):
        # Check if the index already exists in another collection
        index = data.get('index')
        if MeetTeam.objects.filter(index=index).exists():
            raise serializers.ValidationError({"Team Member with this Rank already exists."})
        return data