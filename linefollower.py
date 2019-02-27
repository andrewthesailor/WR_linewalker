from ev3dev.ev3 import *
from time import sleep
from enum import Enum
import time
import math


def run(PCT):
	#print('PTC: ', PCT)
	if PCT == 0:
		rm.run_forever(speed_sp=speedMultiplier * (800))
		lm.run_forever(speed_sp=speedMultiplier * (800))
	elif PCT < 0:
		if PCT < -100:
			PCT = -100
		rm.run_forever(speed_sp=speedMultiplier * (800))
		lm.run_forever(speed_sp=speedMultiplier * (350 + 9 * (PCT + 50)))
	else:
		if PCT > 100:
			PCT = 100
		rm.run_forever(speed_sp=speedMultiplier * (350 + 9 * (50 - PCT)))
		lm.run_forever(speed_sp=speedMultiplier * (800))


def runBigBlack(PCT):
	global speedMultiplier
	#print('PTC: ', PCT)
	
	if PCT == 0:
		rm.run_forever(speed_sp=speedMultiplier * (800))
		lm.run_forever(speed_sp=speedMultiplier * (800))
	elif PCT < 0:
		if PCT < -100:
			PCT = -100
		rm.run_forever(speed_sp=speedMultiplier * (800))
		lm.run_forever(speed_sp=speedMultiplier * (175+12.5 * (PCT + 50)))
	else:
		if PCT > 100:
			PCT = 100
		rm.run_forever(speed_sp=speedMultiplier * (175+12.5 * (50 - PCT)))
		lm.run_forever(speed_sp=speedMultiplier * (800))

def runBigWhite(PCT):
	global speedMultiplier
	#print('PTC: ', PCT)
	
	if PCT == 0:
		rm.run_forever(speed_sp=speedMultiplier * (800))
		lm.run_forever(speed_sp=speedMultiplier * (800))
	elif PCT < 0:
		if PCT < -100:
			PCT = -100
		rm.run_forever(speed_sp=speedMultiplier * (800))
		lm.run_forever(speed_sp=speedMultiplier * (175+12.5 * (PCT + 50)))
	else:
		if PCT > 100:
			PCT = 100
		rm.run_forever(speed_sp=speedMultiplier * (175+12.5 * (50 - PCT)))
		lm.run_forever(speed_sp=speedMultiplier * (800))


i=0
def followLine():
	global lastError, error, lightSensor, lightSensor2, rozniczka, speedMultiplier, white, niedozwolonyCzarny, kp, kd, ki,i 
	lastError = error;
	error = lightSensor.reflected_light_intensity - defaultSensorValue
	rozniczka = (error - lastError)
	speedMultiplier = 0.25
	if lightSensor2.reflected_light_intensity <30:
		if i<100:
			i=i+2
		speedMultiplier=0.25+i*0.0015
		print(speedMultiplier)
		run(0)
	elif lightSensor.reflected_light_intensity > white:
		speedMultiplier = 0.32
		runBigWhite(90)
		if i>0:
			i-=1
	elif lightSensor.reflected_light_intensity < niedozwolonyCzarny:
		speedMultiplier = 0.32
		runBigBlack(-90)
		if i>0:
			i-=1;
	else:
		if i>0:
			i-=1;
		wynik = kp *(error +kd * rozniczka) 
		run(wynik)




lm = LargeMotor('outD')
rm = LargeMotor('outA')
mM= MediumMotor('outC')


speedMultiplier = 0.25



defaultSensorValue = 35;
white = 82

stan = 0

lightSensor = ColorSensor('in1');
assert lightSensor.connected
lightSensor2 = ColorSensor('in2');
kp = 1.6 #1.55
kd = 0.18; # 0.18

niedozwolonyCzarny = 15
error = 0
lastError = 0

lightSensor.mode = 'COL-REFLECT'

lightSensor2.mode = 'COL-REFLECT'

ts = TouchSensor('in3')

rozniczka = 0;
lastError = 0;
lastTime = time.time()
wynik = 0


while ts.is_pressed == False:
	
	followLine()



lm.run_forever(speed_sp=0)
rm.run_forever(speed_sp=0)
