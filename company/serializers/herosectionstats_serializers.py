from rest_framework import serializers
from ..models import HeroSectionStats
import ast
from django.db import transaction

from django.db import transaction

from rest_framework import serializers
from django.db import transaction
from ..models import HeroSectionStats
import ast


class HeroSectionStatsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionStats
        fields = '__all__'

class HeroSectionStatsRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionStats
        fields = '__all__'

class HeroSectionStatsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionStats
        fields = '__all__'


    