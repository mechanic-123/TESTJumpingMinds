from rest_framework import serializers
from .models import *

class ElevatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Elevator
        fields = '__all__'

      
class ElevatorRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElevatorRequest
        fields = ["floor_no"]