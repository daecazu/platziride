"""Circle serializers"""

# Django REST framework

from rest_framework import serializers

class CircleSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()
    members_limit = serializers.IntegerField()

class CreateCircleSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=140)
    slug_name = serializers.SlugField(max_length=40)
    about = serializers.CharField(
        max_length=255,
        required=False
    )