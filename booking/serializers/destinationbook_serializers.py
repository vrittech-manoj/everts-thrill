from rest_framework import serializers
from ..models import DestinationBook
from accounts.models import CustomUser
from airlines.models import Airlines
from activities.models import Activity
from destination.models import Package,Destination
        
class BookingAirlinesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = '__all__'
        
class BookingActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['name']
        
class BookingPackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['name']
        
class BookingDestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['destination_title']

class DestinationBookListSerializers(serializers.ModelSerializer):
    activity = BookingActivitySerializers(read_only = True)
    package = BookingPackageSerializers(read_only = True)
    destination = BookingDestinationSerializers(read_only = True)
    class Meta:
        model = DestinationBook
        fields = '__all__'
        
class DestinationBookRetrieveSerializers(serializers.ModelSerializer):
    activity = BookingActivitySerializers(read_only = True)
    package = BookingPackageSerializers(read_only = True)
    destination = BookingDestinationSerializers(read_only = True)
    class Meta:
        model = DestinationBook
        fields = '__all__'

class DestinationBookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationBook
        fields = '__all__'
        