import numpy as np

## Classes
## Car
class Car:
#   Attributes
    def __init__(self, starting_position, length=5, desired_speed=3.33,\
                other_car):

                self.starting_position = starting_position
                self.length = length
                self.desired_speed = desired_speed
                self.other_car = other_car


#       - starting position
#       - car length
#       - desired speed
#       - other (position & speed)
#   Methods
#       -current position: property??
#       -accelerate: if current speed as distance > distance b/w other car,
#           accelerate @ 2m/s as long as there is room
#       -measures distance b/w other car. Needs location of other car
#       -slow down: if distance is current speed as distance < distance b/w car,
#           match other car's speed
#       -stop: if moving results in colision, stop = speed = 0
#       -randomly slow down: every second, randomly choose to slow down by 2m/s
#        def next_position(self):
#           x_move = self.speed
#           return (self.x + x_move)


## Road
#   Attributes
#       -length of road
#   Methods:


## Simulation
#   Attributes:
#       -cars
#       -Road
#       -captured speed of all cars [numpy array]
#
#   Methods:
#       -reset location when car reaches end of Road
#       -set spacing [numpy array]
#       -create 30 cars [a list]
#       -moves cars
#       -start time
#       -capture speed of all cars at each second
#       -end time
