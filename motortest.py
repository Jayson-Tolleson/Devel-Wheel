#!/usr/bin/env python3
#import required modules
import os, sys
from pyGPIO.gpio import gpio, connector
import time

#set gpio pins
gpio.init()
gpio.setcfg(connector.GPIOp7, 1)  #pin 7 as output pwma
gpio.setcfg(connector.GPIOp11, 1)  #pin 11 as output ain1
gpio.setcfg(connector.GPIOp12, 1)  #pin 12 as output ain2
gpio.setcfg(connector.GPIOp13, 1)  #pin 13 as output stdby
gpio.setcfg(connector.GPIOp15, 1)  #pin 15 as output bin1
gpio.setcfg(connector.GPIOp16, 1)  #pin 16 as output bin2
gpio.setcfg(connector.GPIOp18, 1)  #pin 18 as output pwmb

#drive motor counterclockwise
gpio.output(connector.GPIOp11, 0) #set gpio to low ain1
gpio.output(connector.GPIOp12, 1) #set gpio to high ain2
gpio.output(connector.GPIOp7, 1) #set gpio to high pwma
gpio.output(connector.GPIOp13, 1) #set gpio to high stdby
time.sleep(10)

#reset all gpio pins
gpio.output(connector.GPIOp11, 0) #reset pin11 ain1
gpio.output(connector.GPIOp12, 0) #reset pin12 ain2
gpio.output(connector.GPIOp7, 0) #reset pin7 pwma
gpio.output(connector.GPIOp13, 0) #reset pin13 stdby
gpio.output(connector.GPIOp15, 0) #reset pin15 bin1
gpio.output(connector.GPIOp16, 0) #reset pin16 bin2
gpio.output(connector.GPIOp18, 0) #reset pin18 pwmb

#drive motor clockwise
gpio.output(connector.GPIOp15, 1) #set gpio to low bin1
gpio.output(connector.GPIOp16, 0) #set gpio to high bin2
gpio.output(connector.GPIOp18, 1) #set gpio to high pwmb
gpio.output(connector.GPIOp13, 1) #set gpio to high stdby
time.sleep(15)

#reset all gpio pins
gpio.output(connector.GPIOp11, 0) #reset pin11 ain1
gpio.output(connector.GPIOp12, 0) #reset pin12 ain2
gpio.output(connector.GPIOp7, 0) #reset pin7 pwma
gpio.output(connector.GPIOp13, 0) #reset pin13 stdby
gpio.output(connector.GPIOp15, 0) #reset pin15 bin1
gpio.output(connector.GPIOp16, 0) #reset pin16 bin2
gpio.output(connector.GPIOp18, 0) #reset pin18 pwmb
