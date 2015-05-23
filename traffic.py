import numpy as np
import pprint

########################################################################

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
        return (self.location + self.speed) % 1000

    def move(self):
        self.location = self.next_position()

########################################################################


class Simulation:

    def __init__(self, cars):
        self.cars = cars


    def run(self):

        new_loc = []
        sim = {0: list_starting_pos, }
        tick = 0

        while (tick < 60):
            for idx in range(len(self.cars)):
                self.cars[idx].update_speed(self.cars[((idx + 1)%len(self.cars))])
                self.cars[idx].next_position()
                self.cars[idx].move()
                new_loc.append(self.cars[idx].location)
            sim[tick +1] = new_loc
            new_loc = []
            tick += 1

        return sim
########################################################################


cars = [Car() for _ in range(30)]

starting_pos = np.linspace(0, 1000, len(cars))
list_starting_pos = np.array(starting_pos).tolist()

for car, pos in zip(cars, starting_pos):
    car.location = pos

pprint.pprint(Simulation(cars).run())
