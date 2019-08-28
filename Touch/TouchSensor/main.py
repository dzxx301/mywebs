#!/usr/bin/env python3

from ev3dev.ev3 import *
#from ev3dev.sensor import INPUT_1
#from ev3dev.sensor.lego import TouchSensor
#from ev3dev.led import Leds

ts = TouchSensor()
leds = Leds()

#print("Press the touch sensor to change the LED color!")

while True:
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
