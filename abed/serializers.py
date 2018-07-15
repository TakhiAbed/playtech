from rest_framework import serializers

class PlayerSerializer(serializers.Serializer):
    players = serializers.ListField()

class DetailsSerializer(serializers.Serializer):
    details = serializers.ListField()
