from .models import *




def opendoor(floor_no):
        print("lift door is opening at {}floor".format(floor_no))

def closeddoor(floor_no):
    print("lift door is closing at {}th floor".format(floor_no))

def go_to_floor(elevator_id, current_floor,next_floor_no):
    queryset =  ElevatorRequest.objects.get(elevator_id=elevator_id , floor_no=next_floor_no)
    queryset_elevator = Elevator.objects.get(id= elevator_id)
    if current_floor>next_floor_no:
        queryset_elevator.direction= "down"
        print("Lift is moving downword")
    elif current_floor<next_floor_no:
        queryset_elevator.direction= "up"
        print("lift is moving upword")
         
    opendoor(next_floor_no)
    closeddoor(next_floor_no)
    queryset.delete()
    queryset_elevator.current_floor= next_floor_no
    queryset_elevator.save()

