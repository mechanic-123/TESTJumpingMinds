from django.urls import path
from .views import *

urlpatterns = [
    path("create_elevator/<int:n>/", Main.create_elevator, name="create_elevator"),
    path("", Main.get_elevator, name="get_elevator"),
    path("create_request", Main.create_floor_request, name = 'create_floor_request'),
    path("get_elevator_request/<int:elevator_id>" , Main.get_all_request_of_elevator , name ="get_all_request_of_elevator"),
    path("next_destibation/<int:elevator_id>", Main.get_next_destination, name = 'get_next_destination'),
    path("direction/<int:elevator_id>", Main.get_direction, name = 'get_direction'),
    path("elevator/<int:elevator_id>" ,Main.process_request , name ='process_request')
]
