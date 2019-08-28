#from ev3dev.ev3 import *

#m = Motor("outA")
#m.run_timed(time_sp=3000,speed_sp=500)

# !/usr/bin/env python3
from time import sleep, time
from ev3dev.ev3 import *

mA = LargeMotor("outA")
mB = MediumMotor("outB")

mA.run_forever(speed_sp=900)
mB.run_forever(speed_sp=-1500)
sleep(3)
mA.stop(stop_action="hold")
mB.stop(stop_action="hold")
sleep(1)
mA.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")
mB.run_to_rel_pos(position_sp=-720, speed_sp=1500, stop_action="hold")