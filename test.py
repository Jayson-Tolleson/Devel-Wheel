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
def test()	
  GPIO.output(7, GPIO.HIGH) # Set PWMA
  time.sleep(2)
	GPIO.output(12, GPIO.LOW) # Set AIN1
	GPIO.output(11, GPIO.LOW) # Set AIN2
	GPIO.output(7, GPIO.LOW) # Set PWMA
	GPIO.output(13, GPIO.LOW) # Set STBY
def drive()
  x, y, z = sensor.acceleration
	print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
	orientation = sensor.orientation
	# Orientation is one of these values:if topside:
	# - PL_PUF: Portrait, up, front -------topside, facing front, operable
	# - PL_PUB: Portrait, up, back  -------topside, facing back, operable
	#so, there are conditions now for drive direction of the wheel motion via power
	#tilt ---difference from level on wheeel forward and back
	
	tiltdeg = math.degrees(math.arcos(sqrt(x**2+y**2+z**2)))
  GPIO.output(12, GPIO.LOW) # Set AIN1
	GPIO.output(11, GPIO.LOW) # Set AIN2
	GPIO.output(7, GPIO.LOW) # Set PWMA
	GPIO.output(13, GPIO.LOW) # Set STBY	
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
	GPIO.output(12, GPIO.LOW) # Set AIN1
	GPIO.output(11, GPIO.LOW) # Set AIN2
	GPIO.output(7, GPIO.LOW) # Set PWMA
	GPIO.output(13, GPIO.LOW) # Set STBY
	GPIO.output(12, GPIO.LOW) # Set AIN1
	GPIO.output(11, GPIO.LOW) # Set AIN2
	GPIO.output(7, GPIO.LOW) # Set PWMA
	GPIO.output(13, GPIO.LOW) # Set STBY	
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
  GPIO.output(12, GPIO.LOW) # Set AIN1
	GPIO.output(11, GPIO.LOW) # Set AIN2
	GPIO.output(7, GPIO.LOW) # Set PWMA
	GPIO.output(13, GPIO.LOW) # Set STBY	
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
  time.sleep(1/24)
	GPIO.output(12, GPIO.LOW) # Set AIN1
	GPIO.output(11, GPIO.LOW) # Set AIN2
	GPIO.output(7, GPIO.LOW) # Set PWMA
	GPIO.output(13, GPIO.LOW) # Set STBY
	GPIO.output(12, GPIO.LOW) # Set AIN1
	GPIO.output(11, GPIO.LOW) # Set AIN2
	GPIO.output(7, GPIO.LOW) # Set PWMA
	GPIO.output(13, GPIO.LOW) # Set STBY	
def main():
	sensorsup()
	while True:	
    test()
		drive()	 
main()
