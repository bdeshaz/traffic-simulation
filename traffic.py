import numpy as np


class Car:

    def __init__(self, location, length=5, desired_speed=3.33,\
                speed=0):

                self.location = location
                self.length = length
                self.desired_speed = desired_speed
                self.speed = speed

#   Methods

    def distance(self, next_car):
        return (next_car.position -5) - self.position

    @property
    def position(self):
        return self.location


    @property
    def accelerate(self):
        return self.speed

    @property
    def update_speed(self, next_car):
        if np.random.randint(1,11) == 1:
            if self.speed == 0 or <= 2:
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
                self.speed > self.distance(next_car):
                self.speed = self.speed - self.distance(next_car)

    @property
    def next_position(self):
        return self.location + self.speed

    def move(self):
        self.location = self.next_position



#       -speed:
#           => takes distance
#           accelerate: if current speed as distance > distance b/w other car,
#           accelerate @ 2m/s up to desired_speed as long as there is room
#           slow down: if distance is current speed as distance < distance b/w car,
#           match other car's speed
#           stop: if moving results in colision, stop = speed = 0
#           => returns speed

#       -measures distance b/w other car. Needs location of other car
#           => returns distance

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
    def start_move(self):
        for car in traffic:
            car.begin_move()
#       -start time
#       -capture speed of all cars at each second
#       -end time
