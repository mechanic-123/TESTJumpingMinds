from django.db import models
from datetime import datetime  
# Create your models here.

class Elevator(models.Model):
    is_created = models.DateField(default=datetime.now)
    condition = models.CharField(default="working" , max_length=56)
    direction = models.CharField(default="up" , max_length=5)
    current_floor = models.IntegerField(default=0)
    door_open = models.BooleanField(default=False)

    def __str__(self):
        return  f"{self.id}"
    

class ElevatorRequest(models.Model):
    created_at = models.DateTimeField( default=datetime.now)
    elevator_id = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor_no = models.IntegerField()

    def __str__(self):
        return  f"{self.floor_no}"

