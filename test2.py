from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
from enum import Enum
import time
import math
print("geronimo")
colSenMid = ColorSensor(INPUT_3)
colSenLeft = ColorSensor(INPUT_4)
colSenRight = ColorSensor(INPUT_2)
ts = TouchSensor(INPUT_1)
while not ts.is_pressed :
    print("mid_sen:" + str(colSenMid.reflected_light_intensity))
    print("left_sen:" + str(colSenLeft.reflected_light_intensity))
    print("right_sen:" + str(colSenRight.reflected_light_intensity))
    time.sleep(0.5)

    
