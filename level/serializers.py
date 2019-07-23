from rest_framework import serializers
from .models import Level


class LevelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    level_code = serializers.CharField(
        required=False, allow_blank=True, max_length=11)

    def create(self, validated_data):
        """
        Create and return a new `Level` instance, given the validated data.
        """
        return Level.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing "Level" instance, given the validated data
        """
        instance.name = validated_data.get('name', instance.name)
        instance.level_code = validated_data.get(
            'level_code', instance.level_code)
        instance.save()
        return instance
