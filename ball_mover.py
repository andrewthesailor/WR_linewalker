from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor.lego import ColorSensor


def close_arm() :
	mm.on_for_degrees(SpeedPercent(-100), degrees = 90)
def open_arm() :
	mm.on_for_degrees(SpeedPercent(100), degrees = 100)


def is_line() :
    if (colSenRight.reflected_light_intensity < 15) and (colSenLeft.reflected_light_intensity < 15) :
        return True
    if (colSenRight.reflected_light_intensity > 20) and (colSenLeft.reflected_light_intensity > 20) :
    	return True
    else :
    	return False

def turn() :
	if colSenRight.reflected_light_intensity < 15:
		turn_right()
	if colSenLeft.reflected_light_intensity < 15:
		turn_left()

def go_fwd() :
	tank_drive.on(fwd_pow,fwd_pow)

def turn_right():
	tank_drive.on(turn_pow+12,-2-turn_pow)

def turn_left():

	tank_drive.on(-2-turn_pow,turn_pow+12)

def stop():
		tank_drive.on(0.1,0.1)

def follow_the_line() :

    if is_line() :
    	#if colSenMid.reflected_light_intensity > 70:
    	#	search_for_line()
    	#else:
        go_fwd()
    else:
    	turn() 


def czyMaSkrecic(kolor):
	if colSenRight.color == kolor:
		print("Skręć w prawo")
		return True
	elif colSenLeft.color == kolor:
		print("Skręć w lewo")
		return True
	else:
		print("Coś poszło nie tak")
		return False


#def search_for_line():
#	tank_drive.on(turn_pow,-turn_pow)

turn_pow=14
fwd_pow=20


tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)

colSenRight = ColorSensor(INPUT_2)
colSenMid = ColorSensor(INPUT_3)
colSenLeft = ColorSensor(INPUT_4)

#colSenMid.mode = 'COL-COLOR'


inf = InfraredSensor(INPUT_1)
inf.mode = 'IR-PROX'


print("starting destruction")
while True:
	follow_the_line()
	kolor = colSenMid.color
	#niebieski = colSenMid.blue
	print(kolor)
	if kolor == 5:
		if czyMaSkrecic(5):
			break
	elif kolor == 3:
		if czyMaSkrecic(3):
			break
	elif kolor == 2:
		if czyMaSkrecic(2):
			break

stop()