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

# Initialize a motor at port A.
test_motor = Motor(Port.A)

# Run the motor up to 1000 degrees per second. To a target angle of 720 degrees.
#test_motor.run_target(1000, 720)
test_motor.run_time(1000,10000)

# Play another beep sound.
# This time with a higher pitch (1000 Hz) and longer duration (500 ms).
brick.sound.beep(1000, 500)

# Make the light red
brick.light(Color.RED)

# Wait until any of the buttons are pressed
while not any(brick.buttons()):
    wait(10)

# Do something if the left button is pressed
if Button.LEFT in brick.buttons():
    print("The left button is pressed.")

# Make 5 simple beeps
brick.sound.beeps(5)

brick.display.text("EV3", (60, 50))

brick.display.text("OK")

brick.display.image(ImageFile.EV3_ICON, Align.TOP_RIGHT, clear=False)