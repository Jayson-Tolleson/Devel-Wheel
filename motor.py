TESTING...
#!/usr/bin/env python3
# Import required modules
import cgitb
cgitb.enable
import time
import math
import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_mma8451
import bluetooth
from bluetooth import *
from pprint import pprint
def sensorsup():
	#set up sensors and gpio pins
	# Declare the GPIO settings for the power board
	GPIO.setmode(GPIO.BOARD)
	# Initialize I2C bus. for the accelerometer
	i2c = busio.I2C(board.SCL, board.SDA)
	# Initialize MMA8451 module. the accelerometer
	sensor = adafruit_mma8451.MMA8451(i2c)
	# Optionally change the address if it's not the default:
	#sensor = adafruit_mma8451.MMA8451(i2c, address=0x1C)
	sensor.range = adafruit_mma8451.RANGE_2G # +/- 2G
	sensor.data_rate = adafruit_mma8451.DATARATE_800HZ # 800Hz
	# set up GPIO pins for motor power board
	GPIO.setup(7, GPIO.OUT) # Connected to PWMA
	GPIO.setup(11, GPIO.OUT) # Connected to AIN2
	GPIO.setup(12, GPIO.OUT) # Connected to AIN1
	GPIO.setup(13, GPIO.OUT) # Connected to STBY
	# Set the motor speed
	GPIO.output(7, GPIO.HIGH) # Set PWMA
def bluetooth():
	#connect bluetooth tire pressure monitor for rider on or off ---stem pressure monitor in psi is bluetooth
	hostMACAddress = '00:1f:e1:dd:08:3d' #example address, not the real one
	port = 3 
	backlog = 1
	size = 1024
	s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	s.bind((hostMACAddress, port))
	s.listen(backlog)
	try:
   	 client, clientInfo = s.accept()
   	 while 1:
     	   psi-init = client.recv(size)
		print(psi-init)
	client.close()
     	s.close()
	time.sleep(6)
	try:
   	 client, clientInfo = s.accept()
   	 while 1:
     	   psi = client.recv(size)
		print(psi)
def drive():	
	#start the motor logic if there is a rider weight detected
	if psi>psi-init:
		#find the initial acceleration figure for orientaion and begin conditions for drive motion
		# Main loop to print the acceleration and orientation every second.
		while True:
		x, y, z = sensor.acceleration
		print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
		orientation = sensor.orientation
		# Orientation is one of these values:if topside:
		# - PL_PUF: Portrait, up, front -------topside, facing front, operable
		# - PL_PUB: Portrait, up, back  -------topside, facing back, operable
	#so, there are conditions now for drive direction of the wheel motion via power
		#tilt ---difference from level on wheeel forward and back
		
		tiltdeg = math.degrees(math.arcos(sqrt(x**2+y**2+z**2)))
		
#STBY (standby) coast control for +-5% tilt
		if orientation == adafruit_mma8451.PL_PUF:
			if tiltdeg <=-5:
				# Reset all the GPIO pins by setting them to LOW, including 13, stdby
				GPIO.output(12, GPIO.LOW) # Set AIN1
				GPIO.output(11, GPIO.LOW) # Set AIN2
				GPIO.output(7, GPIO.LOW) # Set PWMA
				GPIO.output(13, GPIO.LOW) # Set STBY	
		if orientation == adafruit_mma8451.PL_PUB:
			if tiltdeg <=5:
				# Reset all the GPIO pins by setting them to LOW, including 13, stdby
				GPIO.output(12, GPIO.LOW) # Set AIN1
				GPIO.output(11, GPIO.LOW) # Set AIN2
				GPIO.output(7, GPIO.LOW) # Set PWMA
				GPIO.output(13, GPIO.LOW) # Set STBY	
#forward
		if orientation == adafruit_mma8451.PL_PUF:
			if tiltdeg >=-5:
			# Drive the motor clockwise with traction control (2wo steps forward and one back) power split up on a 24th of a second
				GPIO.output(12, GPIO.HIGH) # Set AIN1
				GPIO.output(11, GPIO.LOW) # Set AIN2
				time.sleep(1/24)
				GPIO.output(12, GPIO.HIGH) # Set AIN1
				GPIO.output(11, GPIO.LOW) # Set AIN2
				time.sleep(1/24)	
				GPIO.output(12, GPIO.LOW) # Set AIN1
				GPIO.output(11, GPIO.HIGH) # Set AIN2
				time.sleep(1/24)
					if tiltdeg >=-10 #no power supplied, not upright or within+-10 percent tilt, maybe too tilted so no power
					# Reset all the GPIO pins by setting them to LOW
						GPIO.output(12, GPIO.LOW) # Set AIN1
						GPIO.output(11, GPIO.LOW) # Set AIN2
						GPIO.output(7, GPIO.LOW) # Set PWMA
						GPIO.output(13, GPIO.LOW) # Set STBY
		#that is one-eigth of a second of motion forward by stepping two forward one back every 1/24 of a second
		else #no power supplied, not upright or within+-10 percent tilt, maybe too tilted so no power
			GPIO.output(12, GPIO.LOW) # Set AIN1
			GPIO.output(11, GPIO.LOW) # Set AIN2
#REVERSE
		if orientation == adafruit_mma8451.PL_PUB:
			if tiltdeg >=5:
			# Drive the motor counter-clockwise with traction control (2wo steps forward and one back) power split up on a 24th of a second
				GPIO.output(12, GPIO.LOW) # Set AIN1
				GPIO.output(11, GPIO.HIGH) # Set AIN2
				time.sleep(1/24)	
				GPIO.output(12, GPIO.LOW) # Set AIN1
				GPIO.output(11, GPIO.HIGH) # Set AIN2
				time.sleep(1/24)	
				GPIO.output(12, GPIO.HIGH) # Set AIN1
				GPIO.output(11, GPIO.LOW) # Set AIN2
				time.sleep(1/24)
					if tiltdeg >=10: #no power supplied, not upright or within+-10 percent tilt, maybe too tilted so no power
					# Reset all the GPIO pins by setting them to LOW
						GPIO.output(12, GPIO.LOW) # Set AIN1
						GPIO.output(11, GPIO.LOW) # Set AIN2
						GPIO.output(7, GPIO.LOW) # Set PWMA
						GPIO.output(13, GPIO.LOW) # Set STBY
		#that is one-eigth of a second of motion reverse by stepping two back one forward every 1/24 of a second (3 intervals)
		else #no power supplied, not upright or within+-10 percent tilt, maybe too tilted so no power
			GPIO.output(12, GPIO.LOW) # Set AIN1
			GPIO.output(11, GPIO.LOW) # Set AIN2
	else #no rider detected via psi tpms....stop the vehicle
		# Reset all the GPIO pins by setting them to LOW
		GPIO.output(12, GPIO.LOW) # Set AIN1
		GPIO.output(11, GPIO.LOW) # Set AIN2
		GPIO.output(7, GPIO.LOW) # Set PWMA
		GPIO.output(13, GPIO.LOW) # Set STBY
def main():
	sensorsup()
	bluetooth()
	while True:	
		drive()	 
main()
#close socket for bluetooth psi rider monitor
client.close()
s.close()
