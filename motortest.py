#!/usr/bin/env python3
#working script for a two-wire 12v motor on a tb6612 motor driver with a raspberry pi, forward and reverse by switching the poles
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
GPIO.output(27, GPIO.HIGH) #disable standby
time.sleep(5) #run for 5 seconds

#reset all gpio pins
GPIO.output(18, GPIO.LOW) # Set AIN1 
GPIO.output(17, GPIO.LOW) # Set AIN2 
GPIO.output(4, GPIO.LOW) # Set PWMA 
GPIO.output(27, GPIO.LOW) # Set STBY

#set pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) # Connected to PWMA 
GPIO.setup(17, GPIO.OUT) # Connected to AIN2 
GPIO.setup(18, GPIO.OUT) # Connected to AIN1 
GPIO.setup(27, GPIO.OUT) # Connected to STBY

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
