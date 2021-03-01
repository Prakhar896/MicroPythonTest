#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

# Run motor b for 500 degrees
test_motor = Motor(Port.B)
test_motor.run_target(500, 90)

# Play another beep sound.
ev3.speaker.beep(frequency=1000, duration=500)


# START OF EXMAPLE DRIVING BASE PROGRAM: #

# #!/usr/bin/env pybricks-micropython

# """
# Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
# -----------------------------------------------------------------

# This program requires LEGO® EV3 MicroPython v2.0.
# Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

# Building instructions can be found at:
# https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
# """

# from pybricks.hubs import EV3Brick
# from pybricks.ev3devices import Motor
# from pybricks.parameters import Port
# from pybricks.robotics import DriveBase

# def convertFromMetres(metres):
#     return metres * 1000

# # Initialize the EV3 Brick.
# ev3 = EV3Brick()

# # Initialize the motors.
# left_motor = Motor(Port.B)
# right_motor = Motor(Port.C)

# # Initialize the drive base.
# robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# # Go forward and backwards for one meter.
# robot.straight(convertFromMetres(1))
# ev3.speaker.beep()

# robot.straight(convertFromMetres(-1))
# ev3.speaker.beep()

# # Turn clockwise by 360 degrees and back again.
# robot.turn(360)
# ev3.speaker.beep()

# robot.turn(-360)
# ev3.speaker.beep()
