#this file takes the models and translate it into a Json response
from rest_framework import serializers
from .models import Rooms

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms 
        fields = ('id','room_number','room_description','room_type','room_amount','room_status','no_of_beds_available')
        