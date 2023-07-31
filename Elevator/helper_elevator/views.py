from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import  viewsets 
from .serializer  import *
from rest_framework.decorators import api_view
from .viewset import *



class Main(viewsets.ModelViewSet):

    @api_view(['GET'])
    def create_elevator(request,n):
        for i in range(n):
            elevator= Elevator()
            elevator.save()
        return HttpResponse("Successfully Created the Elevator")

    @api_view(['GET'])
    def get_elevator(equest):
        queryset = Elevator.objects.all().delete()
        serializer= ElevatorSerializer(queryset , many=True)
        return HttpResponse(serializer.data ,"  ")

    @api_view(['POST'])
    def create_floor_request(request):
        elevator_id = request.data.get("elevator_id")
        queryset_elevator = Elevator.objects.get(id= elevator_id)
        floor_no = request.data.get("floor_no")
        data=ElevatorRequest(elevator_id=queryset_elevator, floor_no=floor_no)
        data.save()

        return HttpResponse("Your request is successfully Created")
    
    @api_view(['GET'])
    def get_all_request_of_elevator(request, elevator_id):
        queryset = ElevatorRequest.objects.filter(elevator_id=elevator_id).all().order_by("created_at")
        serializer = ElevatorRequestSerializer(queryset , many=True)
        return HttpResponse(serializer.data)
    
    @api_view(['GET'])
    def get_next_destination(request, elevator_id):
        queryset = ElevatorRequest.objects.filter(elevator_id=elevator_id).all().order_by("created_at")[:1]
        serializer = ElevatorRequestSerializer(queryset , many=True)
        return HttpResponse(serializer.data)
    
    @api_view(['GET'])
    def get_direction(request, elevator_id):
        queryset = Elevator.objects.get(id=elevator_id)
        return HttpResponse(f"Direction of Elevator is {queryset.direction}")
    
    @api_view(["Patch"])
    def update_elevator_condition(request):
        elevator_id = request.data.get("elevator_id")
        condition = request.data.get("condition")
        queryset = Elevator.objects.get(id= elevator_id)
        queryset.condition=condition
        queryset.save()

        return HttpResponse("Your request for Elevator condition is successfully Created")


    @api_view(['GET'])
    def process_request(request, elevator_id):
        queryset = ElevatorRequest.objects.filter(elevator_id=elevator_id).all().order_by("created_at")
        
        import pdb;pdb.set_trace()
        if len(queryset)==0:
            return HttpResponse("All request is Fullfilled")

        for query in queryset:
            queryset_elevator = Elevator.objects.get(id= elevator_id)
           
            go_to_floor(elevator_id, queryset_elevator.current_floor,query.floor_no)

        return HttpResponse("All user request for lift is completed")
    

# Create your views here.
