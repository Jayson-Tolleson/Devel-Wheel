#!/usr/bin/env python3

import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) # Connected to PWMA 
GPIO.setup(11, GPIO.OUT) # Connected to AIN2 
GPIO.setup(12, GPIO.OUT) # Connected to AIN1 
GPIO.setup(13, GPIO.OUT) # Connected to STBY
#drive motor clockwise
GPIO.output(12, GPIO.HIGH) # Set AIN1 
GPIO.output(11, GPIO.LOW) # Set AIN2
#set motor speed
GPIO.output(7, GPIO.HIGH) # Set PWMA
#disable standby
GPIO.output(13, GPIO.HIGH)
time.sleep(5) #run for 5 seconds
#drive motor CCW
GPIO.output(12, GPIO.LOW) # Set AIN1 
GPIO.output(11, GPIO.HIGH) # Set AIN2
GPIO.output(7, GPIO.HIGH) # Set PWMA
GPIO.output(13, GPIO.HIGH)
time.sleep(5)
#reset all gpio pins
GPIO.output(12, GPIO.LOW) # Set AIN1 
GPIO.output(11, GPIO.LOW) # Set AIN2 
GPIO.output(7, GPIO.LOW) # Set PWMA 
GPIO.output(13, GPIO.LOW) # Set STBY
