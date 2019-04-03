from ev3dev2.motor import LargeMotor, MediumMotor,OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor.lego import ColorSensor
from time import sleep


zielony = (30, 90, 20)
niebieski = (34, 75, 60)
czerwony = (140, 30 , 10)

granica = 40

def find_starting_pod():
	#dopóki robot nie zauważy zielonej linii
	while get_color(colSenMid) != 1:
		follow_the_line()
	#jeżeli robot zauważy zieloną linię
	if get_color(colSenRight) == 1:
		print("right")
		turn_right()
		sleep(0.7)
	else:
		print("left")
		turn_left()
		sleep(0.7)
	#dopóki robot nie najedzie na czerwone lub niebieskie pole
	while get_color(colSenMid) not in (0,2):
		#print(get_color(colSenMid))
		follow_the_line()
	#weź piłkę
	get_ball()


	
	


def find_target_pod():
	global targetColor
	while get_color(colSenMid) != targetColor:
		follow_the_line()
	if get_color(colSenRight) == targetColor:
		print("right")
		turn_right()
		sleep(1)
	else:
		print("left")
		turn_left()
		sleep(1)
	#
	print("Podążaj za linią")
	follow_the_line()
	sleep(1)
	#
	while get_color(colSenMid) not in (0,2):
		#print(get_color(colSenMid))
		follow_the_line()
	go_fwd()
	sleep(1)
	open_arm()
	#
	go_back()
	sleep(0.8)
	#
	targetColor = 0
	get_out_of_pod_and_reset()


def get_ball():
	print("getting the ball")
	while inf.proximity >= 1:
		print(inf.proximity)
		go_fwd()
	print(inf.proximity)
	print("catch")
	close_arm()
	global targetColor
	targetColor = get_color(colSenMid)
	get_out_of_pod()

def get_out_of_pod():
	tank_drive.on(turn_pow,-turn_pow)
	sleep(3.5)
	print("obrócono")
	tank_drive.off()
	while get_color(colSenMid) != 1:
		follow_the_line()

	while not is_both_black():
		go_fwd()

	turn_right()
	sleep(0.5)
	print("Searching for target pod")
	find_target_pod()

def get_out_of_pod_and_reset():
	tank_drive.on(turn_pow,-turn_pow)
	sleep(3.5)
	print("obrócono")
	tank_drive.off()

	while not is_both_black():
		follow_the_line()

	turn_right()
	sleep(0.7)
	print("Searching for starting pod")
	find_starting_pod()

#0 - czerwony, 1 - zielony, 2 - niebieski
def get_color(sensor):
	kolor = sensor.rgb

	if abs(kolor[0]-zielony[0])+abs(kolor[1]-zielony[1])+abs(kolor[2]-zielony[2]) < granica:
		return 1

	if abs(kolor[0]-czerwony[0])+abs(kolor[1]-czerwony[1])+abs(kolor[2]-czerwony[2]) < granica:
		return 0

	if abs(kolor[0]-niebieski[0])+abs(kolor[1]-niebieski[1])+abs(kolor[2]-niebieski[2]) < granica:
		return 2

	return -1






def close_arm() :
	mm.on_for_degrees(SpeedPercent(-100), degrees = 100)
def open_arm() :
	mm.on_for_degrees(SpeedPercent(100), degrees = 100)


def is_line() :
	if (colSenRight.reflected_light_intensity < 15) and (colSenLeft.reflected_light_intensity < 15) :
		return True
	if (colSenRight.reflected_light_intensity > 20) and (colSenLeft.reflected_light_intensity > 20) :
		return True
	else :
		return False

def is_both_black():
	if (colSenRight.reflected_light_intensity < 15) and (colSenLeft.reflected_light_intensity < 15) :
		return True
	else:
		return False

def turn() :
	if colSenRight.reflected_light_intensity < 15:
		turn_right()
	if colSenLeft.reflected_light_intensity < 15:
		turn_left()

def go_fwd() :
	tank_drive.on(fwd_pow,fwd_pow)

def go_back():
	tank_drive.on(-fwd_pow,-fwd_pow)

def turn_right():
	tank_drive.on(turn_pow+12,-2-turn_pow)

def turn_left():

	tank_drive.on(-2-turn_pow,turn_pow+12)

def follow_the_line() :

	if is_line() :
		#if colSenMid.reflected_light_intensity > 70:
		#	search_for_line()
		#else:
		go_fwd()
	else:
		turn() 




turn_pow=12
fwd_pow=16

mm = MediumMotor(OUTPUT_C)
#tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)
tank_drive = MoveTank(OUTPUT_A,OUTPUT_D)

colSenRight = ColorSensor(INPUT_2)
colSenMid = ColorSensor(INPUT_3)
colSenLeft = ColorSensor(INPUT_4)

#colSenMid.mode = 'COL-COLOR'

targetColor = 0

inf = InfraredSensor(INPUT_1)
inf.mode = 'IR-PROX'

if __name__ == '__main__':
	find_starting_pod()
