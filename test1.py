#from ev3dev2.motor import MediumMotor, OUTPUT_C,SpeedPercent
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
#from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor.lego import ColorSensor

colSenMid = ColorSensor(INPUT_3)

while True:
	print(colSenMid.rgb)
	#print(colSenMid.color)