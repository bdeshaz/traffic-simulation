import numpy as np


class Car:

    def __init__(self, location=0, length=5, desired_speed=3.33,\
                speed=0):

                self.location = location
                self.length = length
                self.desired_speed = desired_speed
                self.speed = speed


    def distance(self, next_car):
        return (next_car.location -5) - self.location

    def update_speed(self, next_car):
        if np.random.randint(1,11) == 1:
            if self.speed == 0 or self.speed <= 2:
                self.speed = 0
            else:
              self.speed = self.speed - 2
        else:
            if self.desired_speed < self.distance(next_car):
                if self.speed < self.desired_speed - 2:
                    self.speed = self.speed + 2
                else:
                    self.speed = self.desired_speed
            elif self.speed < self.distance(next_car):
                self.speed = self.speed + (self.distance(next_car) - self.speed)
            elif self.speed == self.distance(next_car):
                self.speed = next_car.speed
            else:
                self.speed = self.speed - self.distance(next_car)


    def next_position(self):
        return self.location + self.speed

    def move(self):
        self.location = self.next_position()


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
#       -moves cars
    def start_move(self):
        for car in self.traffic:
            car.begin_move()
#       -start time
#       -capture speed of all cars at each second
#       -end time

## Outside the Simulation
traffic = []
