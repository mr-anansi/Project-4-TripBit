from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Town, Trip, Badge, Group
User = get_user_model()

class UserSerializer(serializers.ModelSerializer): # This user serializer is used to populate a nested owner on a post or comment

    class Meta:
        model = User
        fields = ('id', 'name')


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('id', 'name', 'start_date', 'end_date', 'user')

class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = ('id', 'name', 'description', 'image')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'owner', 'members', 'requests', 'podium_1_user', 'podium_2_user', 'podium_3_user', 'podium_1_score', 'podium_2_score', 'podium_3_score')
        extra_kwargs = {
            'members': {'required': False},
            'requests': {'required': False},
            'podium_1_user': {'required': False},
            'podium_2_user': {'required': False},
            'podium_3_user': {'required': False},
            'podium_1_score': {'required': False},
            'podium_2_score': {'required': False},
            'podium_3_score': {'required': False}
        }
    