from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
from enum import Enum
import time
import math


def is_line() :

    if (colSenRight.reflected_light_intensity < 15) and (colSenLeft.reflected_light_intensity < 15) :
        print("black")
        return True
    if (colSenRight.reflected_light_intensity > 20) and (colSenLeft.reflected_light_intensity > 20) :
    	print("white")
    	return True
    else :
    	print(colSenRight.reflected_light_intensity)
    	print(colSenLeft.reflected_light_intensity)
    	print("fuck")
    	return False

def turn() :
	if colSenRight.reflected_light_intensity < 15:
		print("turn right")
		turn_right()
	#if prevRight < 10 :
	#	turn_right()
	if colSenLeft.reflected_light_intensity < 15:
		print("turn left")
		turn_left()

def go_fwd() :
	print("gogogo")
	tank_drive.on(fwd_pow,fwd_pow)
#	motorLeft.on_for_seconds(70,0.1)
#	motorRight.on_for_seconds(70,0.1)


def turn_right():
#	motorLeft.on_for_seconds(70,0.4)
	tank_drive.on(turn_pow+10,-(turn_pow))

def turn_left():
#	motorRight.on_for_seconds(70,0.4)
	tank_drive.on(-(turn_pow),turn_pow+10)

def stop():
		tank_drive.on(0.1,0.1)
#	motorLeft.run_forever(speed_sp = 0)
#	motorRight.run_forever(speed_sp = 0)

#def out_of_line():
#	return (not is_line(colSenMid)) and (not is_line(colSenRight)) and (not is_line(colSenLeft))

def follow_the_line() :

    #if out_of_line:
    #    print("out of bounds")
    if is_line() :
        go_fwd()
    #else:
    #	stop()
    else:
    	turn() 
    prevRight=colSenRight.reflected_light_intensity



turn_pow=25
fwd_pow=20


#motorRight=LargeMotor(OUTPUT_A)
#motorLeft=LargeMotor(OUTPUT_B)
tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)

colSenRight = ColorSensor(INPUT_2)
colSenMid = ColorSensor(INPUT_3)
colSenLeft = ColorSensor(INPUT_4)


ts = TouchSensor(INPUT_1)

prevRight = 20

print("starting destruction")
while not ts.is_pressed :
    follow_the_line()

stop()