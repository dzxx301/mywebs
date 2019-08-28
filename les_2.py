#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep, time
import traceback

try:
    lcd = Screen()
    lcd.clear()
    intX = 10
    intY = 5

    lcd.draw.text((intX, intY), 'Hello World')
    lcd.draw.rectangle((20, 20, 158, 40), fill = 'black')
    lcd.draw.text((25, 25), 'Hello World', fill = 'white')
    lcd.update()

    sleep(10)

except:
    # If there is any error, it will be stored in the log file in the same directory
    logtime = str(time())
    f=open("log" + logtime + ".txt",'a')
    traceback.print_exc(file=f)
    f.flush()
    f.close()
