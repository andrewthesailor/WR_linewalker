from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor

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
	if colSenLeft.reflected_light_intensity < 15:
		print("turn left")
		turn_left()

def go_fwd() :
	tank_drive.on(fwd_pow,fwd_pow)
def turn_right():
	tank_drive.on(turn_pow+8,-turn_pow)

def turn_left():

	tank_drive.on(-turn_pow,turn_pow+8)

def stop():
		tank_drive.on(0.1,0.1)

def follow_the_line() :

    if is_line() :
    	if colSenMid.reflected_light_intensity > 70:
    		print(colSenMid.reflected_light_intensity)
    		search_for_line()
    	else:
        	go_fwd()
    else:
    	turn() 


def search_for_line():
	tank_drive.on(turn_pow,-turn_pow)

turn_pow=14
fwd_pow=27


tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)

colSenRight = ColorSensor(INPUT_2)
colSenMid = ColorSensor(INPUT_3)
colSenLeft = ColorSensor(INPUT_4)


ts = TouchSensor(INPUT_1)


print("starting destruction")
while not ts.is_pressed :
	follow_the_line()

stop()