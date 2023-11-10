from rest_framework import serializers
from .models import Invitation, Room, House
from polls.models import OlaroomProfile
from .choices import *

class ChoiceField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoiceField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class InvitationSerializer(serializers.ModelSerializer):
    room_type = RoomSerializer()
    visited_for = ChoiceField(choices=VISITED_FOR)
    occupation = ChoiceField(choices=OCCUPATION)
    class Meta:
        model = Invitation
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OlaroomProfile
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__" 