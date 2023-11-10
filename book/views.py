from django.shortcuts import render, get_object_or_404
from .models import Invitation, Room, Notification
from polls.models import OlaroomProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RoomSerializer, ProfileSerializer

@api_view(['GET'])
def our_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)