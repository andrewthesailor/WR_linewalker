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
	if kolor is "Zielony":
		if czyZielony(colSenRight):
			print("Skręć w prawo")
			return
		elif czyZielony(colSenLeft):
			print("Skręć w lewo")
			return
		else:
			print("Błąd przy skręcaniu")
			return
	elif kolor is "Czerwony":
		if czyCzerwony(colSenRight):
			print("Skręć w prawo")
			return
		elif czyCzerwony(colSenLeft):
			print("Skręć w lewo")
			return
		else:
			print("Błąd przy skręcaniu")
			return
	elif kolor is "Niebieski":
		if czyNiebieski(colSenRight):
			print("Skręć w prawo")
			return
		elif czyNiebieski(colSenLeft):
			print("Skręć w lewo")
			return
		else:
			print("Błąd przy skręcaniu")
			return


#def search_for_line():
#	tank_drive.on(turn_pow,-turn_pow)

turn_pow=14
fwd_pow=20


tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)

colSenRight = ColorSensor(INPUT_2)
colSenMid = ColorSensor(INPUT_3)
colSenLeft = ColorSensor(INPUT_4)

czarny = (24, 30, 11)
biały = (155, 200, 100)
zielony = (30, 90, 20)
niebieski = (34, 75, 60)
czerwony = (140, 30 , 10)

granica = 40

#colSenMid.mode = 'COL-COLOR'


inf = InfraredSensor(INPUT_1)
inf.mode = 'IR-PROX'

def czyZielony(sensor):
	kolor = sensor.rgb
	if abs(kolor[0]-zielony[0])+abs(kolor[1]-zielony[1])+abs(kolor[2]-zielony[2]) < granica:
		return True
	else:
		return False

def czyCzerwony(sensor):
	kolor = sensor.rgb
	if abs(kolor[0]-czerwony[0])+abs(kolor[1]-czerwony[1])+abs(kolor[2]-czerwony[2]) < granica:
		return True
	else:
		return False

def czyNiebieski(sensor):
	kolor = sensor.rgb
	if abs(kolor[0]-niebieski[0])+abs(kolor[1]-niebieski[1])+abs(kolor[2]-niebieski[2]) < granica:
		return True
	else:
		return False


print("starting destruction")
while True:
	follow_the_line()

	#Czarny
	#if abs(kolor[0]-czarny[0])+abs(kolor[1]-czarny[1])+abs(kolor[2]-czarny[2]) < granica:
	#	print("Czarny")
	#Biały
	#elif abs(kolor[0]-biały[0])+abs(kolor[1]-biały[1])+abs(kolor[2]-biały[2]) < granica:
	#	print("Biały")
	#Zielony
	if czyZielony(colSenMid):
		print("Zielony")
		czyMaSkrecic("Zielony")
		break
	#Niebieski
	elif czyNiebieski(colSenMid):
		print("Niebieski")
		czyMaSkrecic("Niebieski")
		break
	#Czerwony
	elif czyCzerwony(colSenMid):
		print("Czerwony")
		czyMaSkrecic("Czerwony")
		break

stop()