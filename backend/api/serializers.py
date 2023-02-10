from rest_framework import serializers

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)