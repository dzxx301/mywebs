#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

motor = Motor(Port.A)
#motor.run_time(800,5000)

# Wait until any of the buttons are pressed
while not any(brick.buttons()):
    wait(10)

# Do something if the right button is pressed
if Button.RIGHT in brick.buttons():
    print("The right button is pressed.")
    motor.run_time(800,5000)
else:
    print("The other button is pressed")
    motor.run_time(-800,5000)

# Make 5 simple beeps
brick.sound.beeps(5)