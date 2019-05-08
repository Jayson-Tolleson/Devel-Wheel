#!/usr/bin/env python3

import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) # Connected to PWMA 
GPIO.setup(17, GPIO.OUT) # Connected to AIN2 
GPIO.setup(18, GPIO.OUT) # Connected to AIN1 
GPIO.setup(27, GPIO.OUT) # Connected to STBY
#drive motor clockwise
GPIO.output(18, GPIO.HIGH) # Set AIN1 
GPIO.output(17, GPIO.LOW) # Set AIN2
#set motor speed
GPIO.output(4, GPIO.HIGH) # Set PWMA
#disable standby
GPIO.output(27, GPIO.HIGH)
time.sleep(5) #run for 5 seconds
#drive motor CCW
GPIO.output(18, GPIO.LOW) # Set AIN1 
GPIO.output(17, GPIO.HIGH) # Set AIN2
GPIO.output(4, GPIO.HIGH) # Set PWMA
GPIO.output(27, GPIO.HIGH)
time.sleep(5)
#reset all gpio pins
GPIO.output(18, GPIO.LOW) # Set AIN1 
GPIO.output(17, GPIO.LOW) # Set AIN2 
GPIO.output(4, GPIO.LOW) # Set PWMA 
GPIO.output(27, GPIO.LOW) # Set STBY
