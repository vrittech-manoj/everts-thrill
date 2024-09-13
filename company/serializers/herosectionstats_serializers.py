from rest_framework import serializers
from ..models import HeroSectionStats
import ast
from django.db import transaction

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

    def to_internal_value(self, data):
        """
        Converts the incoming nested dictionary (or list of dictionaries) into 
        a format suitable for the serializer.
        """
        if isinstance(data, dict):
            stats = data.get('stats', [])
            if isinstance(stats, list):
                return [super().to_internal_value(item) for item in stats]
        return super().to_internal_value(data)

    @transaction.atomic
    def create(self, validated_data):
        """
        Handles bulk creation if validated_data is a list of dictionaries.
        """
        if isinstance(validated_data, list):
            stats = HeroSectionStats.objects.bulk_create(
                [HeroSectionStats(**item) for item in validated_data]
            )
            return stats
        else:
            stat = HeroSectionStats.objects.create(**validated_data)
            return stat

    @transaction.atomic
    def update(self, instance, validated_data):
        """
        Handles bulk update if validated_data is a list.
        """
        if isinstance(validated_data, list):
            existing_stats = {stat.id: stat for stat in instance}
            updated_stats = []

            for stat_data in validated_data:
                stat_id = stat_data.get('id', None)
                if stat_id and stat_id in existing_stats:
                    stat_instance = existing_stats[stat_id]
                    for attr, value in stat_data.items():
                        setattr(stat_instance, attr, value)
                    stat_instance.save()
                    updated_stats.append(stat_instance)
                else:
                    new_stat = HeroSectionStats.objects.create(**stat_data)
                    updated_stats.append(new_stat)

            return updated_stats
        else:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            return instance
