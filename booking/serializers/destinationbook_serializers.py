from rest_framework import serializers
from ..models import DestinationBook
from accounts.models import CustomUser
from airlines.models import Airlines
from activities.models import Activity
from destination.models import Package,Destination

class BookingUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name','phone','email']
        
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
    user = BookingUserSerializers(read_only = True)
    # airlines = BookingAirlinesSerializers(read_only = True)
    activity = BookingActivitySerializers(read_only = True)
    package = BookingPackageSerializers(read_only = True)
    destination = BookingDestinationSerializers(read_only = True)
    class Meta:
        model = DestinationBook
        fields = '__all__'
        
class DestinationBookRetrieveSerializers(serializers.ModelSerializer):
    user = BookingUserSerializers(read_only = True)
    # airlines = BookingAirlinesSerializers(read_only = True)
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
        
        
    # user_booking = BookingUserSerializers(read_only = True)
    # airlines_booking = BookingAirlinesSerializers(read_only = True)
    # activity_booking = BookingActivitySerializers(read_only = True)
    # package_booking = BookingPackageSerializers(read_only = True)
    # destination_book = BookingDestinationSerializers(read_only = True)