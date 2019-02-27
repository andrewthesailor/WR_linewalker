from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
print("geronimo")
colSen = ColorSensor(INPUT_1)
m=LargeMotor(OUTPUT_A)
while 1<2:
    if colSen.reflected_light_intensity<50 :
        m.run_forever(speed_sp=40)
    else:
        m.run_forever(speed_sp=0)
