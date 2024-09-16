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