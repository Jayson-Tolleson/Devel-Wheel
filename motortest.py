#!/usr/bin/env python3
#import required modules
import time
import pigpio
#works on pi and le potato and asus tinkerboard
# Connect to local Pi.
pi = pigpio.pi() 

#set gpio pins
pi.set_mode(7, pigpio.OUTPUT)  #pin 7 as output pwma
pi.set_mode(11, pigpio.OUTPUT) #pin 11 as output ain1
pi.set_mode(12, pigpio.OUTPUT) #pin 12 as output ain2
pi.set_mode(13, pigpio.OUTPUT) #pin 13 as output stdby
pi.set_mode(15, pigpio.OUTPUT) #pin 15 as output bin1
pi.set_mode(16, pigpio.OUTPUT) #pin 16 as output bin2
pi.set_mode(18, pigpio.OUTPUT) #pin 18 as output pwmb

#drive motor counterclockwise
pi.write(11,0) #set gpio11 to low ain1
pi.write(12,1) #set gpio12 to low ain2
pi.write(7,1)  #set gpio7 to high pwma
pi.write(13,1) #set gpio13 to high stby
time.sleep(10) #run for 10,000 ms

#reset all gpio pins
pi.write(11, 0) #reset pin11 ain1
pi.write(12, 0) #reset pin12 ain2
pi.write(7, 0) #reset pin7 pwma
pi.write(13, 0) #reset pin13 stdby
pi.write(15, 0) #reset pin15 bin1
pi.write(16, 0) #reset pin16 bin2
pi.write(18, 0) #reset pin18 pwmb

#drive motor clockwise
pi.write(15, 1) #set gpio to low bin1
pi.write(16, 0) #set gpio to high bin2
pi.write(18, 1) #set gpio to high pwmb
pi.write(13, 1) #set gpio to high stdby
time.sleep(15)  #run for 15,000 ms

#reset all gpio pins
pi.write(11, 0) #reset pin11 ain1
pi.write(12, 0) #reset pin12 ain2
pi.write(7, 0) #reset pin7 pwma
pi.write(13, 0) #reset pin13 stdby
pi.write(15, 0) #reset pin15 bin1
pi.write(16, 0) #reset pin16 bin2
pi.write(18, 0) #reset pin18 pwmb
