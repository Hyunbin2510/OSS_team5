#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
import time

ev3 = EV3Brick()


left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.S1)


wheel_diameter = 5.6
axle_track = 115

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


def check_for_red():
    if color_sensor.color() == Color.RED:
        return True
    return False


while True:
    if check_for_red(): 
        robot.drive(-100, 0) 
        time.sleep(3) 
        robot.stop()  
        break 
    else:
        robot.drive(50, 0) 
