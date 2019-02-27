from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
import time
print("geronimo")
colSenMid = ColorSensor(INPUT_1)
colSenLeft = ColorSensor(INPUT_2)
colSenRight = ColorSensor(INPUT_3)
while 1<2:
    print("mid_sen:" + str(colSenMid.reflected_light_intensity))
    print("left_sen:" + str(colSenLeft.reflected_light_intensity))
    print("right_sen:" + str(colSenRight.reflected_light_intensity))
    time.sleep(0.5)

    
