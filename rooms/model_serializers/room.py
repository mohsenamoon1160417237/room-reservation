from rest_framework import serializers
from rooms.models.room import Room


class RoomCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Room
        fields = ['name', 'chair_number']

    def create(self, validated_data):

        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.chair_number = validated_data.get('chair_number', instance.chair_number)
        instance.save()
        return instance
