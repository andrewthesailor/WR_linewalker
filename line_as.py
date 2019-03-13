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
        return True
    if (colSenRight.reflected_light_intensity > 20) and (colSenLeft.reflected_light_intensity > 20) :
    	return True
    else :
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
	else:
		turn_by_memory()
	
def turn_by_memory():
	if prevRight < 15:
		turn_right()
	if prevLeft <15:
		turn_left()

def go_fwd() :
	tank_drive.on(fwd_pow-(diff()),fwd_pow+(diff()))
	resp=diff()/2
#	motorLeft.on_for_seconds(70,0.1)
#	motorRight.on_for_seconds(70,0.1)


def turn_right():
#	motorLeft.on_for_seconds(70,0.4)
	tank_drive.on(turn_pow+10,-turn_pow)

def turn_left():
#	motorRight.on_for_seconds(70,0.4)
	tank_drive.on(-turn_pow,turn_pow+10)

def stop():
		tank_drive.on(0.1,0.1)
#	motorLeft.run_forever(speed_sp = 0)
#	motorRight.run_forever(speed_sp = 0)

#def out_of_line():
#	return (not is_line(colSenMid)) and (not is_line(colSenRight)) and (not is_line(colSenLeft))

#def check_if_out():
#	values = [colSenRight.reflected_light_intensity, colSenLeft.reflected_light_intensity, colSenMid.reflected_light_intensity]
#	two_max = sorted(values)[:2]
#	suma = sum(two_max)
#	print(str(suma))
#	if suma > 95:
#		print("search for shit")
#		return True
#	else:
#		return False

def diff():
	#return (colSenRight.reflected_light_intensity-colSenLeft.reflected_light_intensity)/20
	return 0
def follow_the_line() :

    #if out_of_line:
    #    print("out of bounds")
    if is_line() :
    	if colSenMid.reflected_light_intensity > 60:
    		print(colSenMid.reflected_light_intensity)
    		search_for_line()
    	else:
        	go_fwd()
    #else:
    #	stop()
    else:
    	turn() 
#	prevRight=colSenRight.reflected_light_intensity
#	prevLeft = colSenLeft.reflected_light_intensity

def search_for_line():
	tank_drive.on(turn_pow,-turn_pow)

turn_pow=25
fwd_pow=20
resp=0

#motorRight=LargeMotor(OUTPUT_A)
#motorLeft=LargeMotor(OUTPUT_B)
tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)

colSenRight = ColorSensor(INPUT_2)
colSenMid = ColorSensor(INPUT_3)
colSenLeft = ColorSensor(INPUT_4)


ts = TouchSensor(INPUT_1)

prevRight = 20
prevLeft = 20


print("starting destruction")
while not ts.is_pressed :
	#if check_if_out() :
	#	search_for_line()
	#else:
	follow_the_line()

stop()