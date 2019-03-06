from ev3dev.ev3 import *
from time import sleep
from enum import Enum
import time
import math


def is_line(sensor) :
    if sensor.reflected_light_intensity < 30 :
        return True
    return False

def is_turn_right() :
    if colSenRight.reflected_light_intensity < colSenLeft.reflected_light_intensity:
        return True
    return False

def go_fwd() :
    motorLeft.run_forever(speed_sp = 100)
    motorRight.run_forever(speed_sp = 100)


def turn_right():
    motorLeft.run_forever(speed_sp = )
    motorRight.run_forever(speed_sp = )

def turn_left():
    motorLeft.run_forever(speed_sp = )
    motorRight.run_forever(speed_sp = )


def follow_the_line() :
    if is_line(colSenMid) :
        go_fwd()
    elif is_turn_right() :
        turn_right()
    turn_left()







motorLeft=LargeMotor(OUTPUT_A)
motorRight=LargeMotor(OUTPUT_B)

colSenLeft = ColorSensor(INPUT_1)
colSenMid = ColorSensor(INPUT_2)
colSenRight = ColorSensor(INPUT_3)
ts = TouchSensor(INPUT_4)


while ts.is_pressed() == False :
    follow_the_line()

motorLeft.run_forever(speed_sp = 0)
motorRight.run_forever(speed_sp = 0)