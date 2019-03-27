from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D, MediumMotor, OUTPUT_B, SpeedPercent
from ev3dev2.sensor import INPUT_2, INPUT_1, INPUT_4, INPUT_3
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.button import Button
from time import sleep
from ev3dev2.sound import Sound


mm = MediumMotor (OUTPUT_B)
IS = InfraredSensor( INPUT_3 )
tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)
cl1 = ColorSensor(INPUT_1) #prawy 
cl2 = ColorSensor(INPUT_4) #lewy
ts = TouchSensor(INPUT_2)
cl1.mode = "COL-COLOR"
cl2.mode = "COL-REFLECT"
sound = Sound()


PickUpColor = 3
PutDownColor = 5
valueOfIS = 7
white = 47
black = 6
target = (white+black)/2 #light value 
lastError = 0
error = 0
integral = 0

kp = 0.65#0.6
ki = 0.45#0.2
kd = 2.75#2.7


INTEGRAL_MAX = 100
MAX_SPEED = -55
TARGET_SPEED = 0.25 * MAX_SPEED #0.3
MIN_SPEED = -10




def Stop():
	tank_pair.off()
	sleep(2)
	sound.beep()

def FollowTheLine():
	error = target - cl2.reflected_light_intensity
	integral = integral + error
	derivative = error - lastError
	lastError = error
	correction = kp * error + ki * integral + kd * derivative

	if integral > INTEGRAL_MAX:
		integral = INTEGRAL_MAX
	elif integral < -INTEGRAL_MAX:
		integral = -INTEGRAL_MAX

	if TARGET_SPEED - abs(correction) < MAX_SPEED:
		if correction < 0:
			correction = MAX_SPEED - TARGET_SPEED
		else:
			correction = TARGET_SPEED - MAX_SPEED
	if ( correction > 34 and cl1.color == 1):
		tank_pair.on(left_speed = -7.5, right_speed = -7.5)
		sleep(0.5) #0.3
	tank_pair.on(left_speed = 0.2*(TARGET_SPEED + correction), right_speed = 0.2*(TARGET_SPEED - correction))


def PickUp():
	mm.on_for_seconds( SpeedPercent(100), 1.4)


def PutDown():
	mm.on_for_seconds( SpeedPercent(-100), 1.4)

def FindingColor(color):
	flag = False
	tank_pair.on( left_speed = -10, right_speed = 0) 
	Stop()		
def FindingColor2(color):
	flag = False
	tank_pair.on( left_speed = -10, right_speed = 0) #KALIBRACJA tak zeby byl o 90 stopni skret w prawo
	sleep(0.1) #KALIBRACJA trzeba skalibrowac zeby opsucil zielony poprawny
	Stop()
	if cl1.color == color: # znajdowanie koloru po prawej stronie i ustawienie flagi
		flag = True
	tank_pair.off()
	
	if flag == True:
		tank_pair.on( left_speed = -10, right_speed = -5)
		sleep(0.5)
		Stop()
		tank_pair.off()
	else:
		tank_pair.on( left_speed = 10, right_speed = 0)
		sleep(0.1)
		Stop()
		tank_pair.on( left_speed = 0, right_speed = -10)
		sleep(0.6)
		Stop()


while not False:
	error = target - cl2.reflected_light_intensity
	integral = integral + error
	derivative = error - lastError
	lastError = error
	correction = kp * error + ki * integral + kd * derivative

	if integral > INTEGRAL_MAX:
		integral = INTEGRAL_MAX
	elif integral < -INTEGRAL_MAX:
		integral = -INTEGRAL_MAX

	if TARGET_SPEED - abs(correction) < MAX_SPEED:
		if correction < 0:
			correction = MAX_SPEED - TARGET_SPEED
		else:
			correction = TARGET_SPEED - MAX_SPEED
	tank_pair.on(left_speed = 0.2*(TARGET_SPEED + correction), right_speed = 0.2*(TARGET_SPEED - correction))
	if ( cl1.color == PickUpColor):
		tank_pair.on(left_speed = -10, right_speed = -3)
		sleep(2.2)
		while (cl1.color != PickUpColor):
			error = target - cl2.reflected_light_intensity
			integral = integral + error
			derivative = error - lastError
			lastError = error
			correction = kp * error + ki * integral + kd * derivative

			if integral > INTEGRAL_MAX:
				integral = INTEGRAL_MAX
			elif integral < -INTEGRAL_MAX:
				integral = -INTEGRAL_MAX

			if TARGET_SPEED - abs(correction) < MAX_SPEED:
				if correction < 0:
					correction = MAX_SPEED - TARGET_SPEED
				else:
					correction = TARGET_SPEED - MAX_SPEED
			tank_pair.on(left_speed = 0.2*(TARGET_SPEED + correction), right_speed = 0.2*(TARGET_SPEED - correction))
		tank_pair.off()
		PickUp()
		tank_pair.on(left_speed = -5, right_speed = 5)
		sleep(5)
		while ( cl1.color != PickUpColor):
			error = target - cl2.reflected_light_intensity
			integral = integral + error
			derivative = error - lastError
			lastError = error
			correction = kp * error + ki * integral + kd * derivative

			if integral > INTEGRAL_MAX:
				integral = INTEGRAL_MAX
			elif integral < -INTEGRAL_MAX:
				integral = -INTEGRAL_MAX

			if TARGET_SPEED - abs(correction) < MAX_SPEED:
				if correction < 0:
					correction = MAX_SPEED - TARGET_SPEED
				else:
					correction = TARGET_SPEED - MAX_SPEED
			tank_pair.on(left_speed = 0.2*(TARGET_SPEED + correction), right_speed = 0.2*(TARGET_SPEED - correction))
		if ( cl1.color == PickUpColor):
			tank_pair.on(left_speed = -3, right_speed = -10)
			sleep(2.2)
		while ( cl1.color != PutDownColor):
			error = target - cl2.reflected_light_intensity
			integral = integral + error
			derivative = error - lastError
			lastError = error
			correction = kp * error + ki * integral + kd * derivative

			if integral > INTEGRAL_MAX:
				integral = INTEGRAL_MAX
			elif integral < -INTEGRAL_MAX:
				integral = -INTEGRAL_MAX

			if TARGET_SPEED - abs(correction) < MAX_SPEED:
				if correction < 0:
					correction = MAX_SPEED - TARGET_SPEED
				else:
					correction = TARGET_SPEED - MAX_SPEED
			tank_pair.on(left_speed = 0.2*(TARGET_SPEED + correction), right_speed = 0.2*(TARGET_SPEED - correction))
			break
PutDown()
tank_pair.off()