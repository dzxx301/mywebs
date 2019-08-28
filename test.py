#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep, time
#from ev3dev.led import Leds

Sound.beep(5)
sleep(1)
Sound.set_volume(100)
Sound.speak('Welcome to the E V 3 dev project!').wait()

mA = MediumMotor('outA')
mA.run_forever(speed_sp=600)
sleep(5)
mA.run_timed(time_sp=1000)
sleep(5)
mA.stop(stop_action='hold')
sleep(5)
#mA.run_to_rel_pos(position_sp=720,speed_sp=200,stop_action='hold')
mA.run_forever(speed_sp=-600)
sleep(5)

Leds.set_color(color='RED')
