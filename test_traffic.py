from traffic import *

car_1 = Car(location=0)


car_2 = Car(location = 7)

def test_distance():
    assert car_1.distance(car_2) == 2

def test_update_speed():
    """ Without possibility of a random slow down"""
    car_1.update_speed(car_2)
    assert car_1.speed == 2

def test_next_position():
    assert car_1.next_position() == 2

def test_move():
    car_1.move()
    assert car_1.location == 2
