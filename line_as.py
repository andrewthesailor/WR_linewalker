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
    if colSenRight.reflected_light_intensity < 30:
        return True
    return False

def go_fwd() :
    motorLeft.run_forever(speed_sp = 100)
    motorRight.run_forever(speed_sp = 100)


def turn_right():
    motorLeft.run_forever(speed_sp = 200)
    motorRight.run_forever(speed_sp = 0)

def turn_left():
    motorLeft.run_forever(speed_sp = 0)
    motorRight.run_forever(speed_sp = 200)


def follow_the_line() :
    if out_of_line:
        print("out of bounds")
    elif is_line(colSenMid) :
        go_fwd()
    elif is_turn_right() :
        turn_right()
    else :
        turn_left()






motorRight=LargeMotor(OUTPUT_A)
motorLeft=LargeMotor(OUTPUT_B)

colSenRight = ColorSensor(INPUT_2)
colSenMid = ColorSensor(INPUT_3)
colSenLeft = ColorSensor(INPUT_4)


ts = TouchSensor(INPUT_1)


while not ts.is_pressed :
    follow_the_line()

motorLeft.run_forever(speed_sp = 0)
motorRight.run_forever(speed_sp = 0)