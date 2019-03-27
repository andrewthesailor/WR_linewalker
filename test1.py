#from ev3dev2.motor import MediumMotor, OUTPUT_C,SpeedPercent
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
#from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor.lego import ColorSensor

colSenMid = ColorSensor(INPUT_3)

czarny = (24, 30, 11)
biały = (155, 200, 100)
zielony = (30, 90, 20)
niebieski = (34, 75, 60)
czerwony = (140, 30 , 10)

granica = 40

while True:
	kolor = colSenMid.rgb
	print(kolor)
	Czarny
	if abs(kolor[0]-czarny[0])+abs(kolor[1]-czarny[1])+abs(kolor[2]-czarny[2]) < granica:
		print("Czarny")
	Biały
	elif abs(kolor[0]-biały[0])+abs(kolor[1]-biały[1])+abs(kolor[2]-biały[2]) < granica:
		print("Biały")
	#Zielony
	elif abs(kolor[0]-zielony[0])+abs(kolor[1]-zielony[1])+abs(kolor[2]-zielony[2]) < granica:
		print("Zielony")
	#Niebieski
	elif abs(kolor[0]-niebieski[0])+abs(kolor[1]-niebieski[1])+abs(kolor[2]-niebieski[2]) < granica:
		print("Niebieski")
	#Czerwony
	elif abs(kolor[0]-czerwony[0])+abs(kolor[1]-czerwony[1])+abs(kolor[2]-czerwony[2]) < granica:
		print("Czerwony")
	#Błąd
	else:
		print("Błąd")
	