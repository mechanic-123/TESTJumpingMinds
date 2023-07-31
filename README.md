# TESTJumpingMinds


1. To create Elevator url =>
url ==>> Get,  "create_elevator/n"
n= number of elevator

2.Fetch all requests for a given elevator
url ==>> Get, ""

3. Fetch the next destination floor for a given elevator
 url ==>>Get, "next_destibation/id"
  id = elevator_id

4.Fetch if the elevator is moving up or down currently
url ==>>Get, "direction/id"
id = elevator_id

5.Saves user request to the list of requests for a elevator
url ==>>post  , "create_floor_request"
body_param= {
    "elevator_id" : 1,
    "floor_no" : 2
}

6. Mark a elevator as not working or in maintenance
url ==>> Patch  "update_condition"
  body_param ={
    "elevator_id" : 1,
    "condition" : "not working
   }

7 . Main Api for working Lift
url ==>> Get "elevator/id"
id = elevator_id
