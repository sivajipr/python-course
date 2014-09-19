#P1.6 is GND
#P1.8 is OUTPUT
#Blink LED on P1.8

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(8, gpio.OUT)

while True:
        gpio.output(8, gpio.HIGH)
        time.sleep(.1)
        gpio.output(8, gpio.LOW)
        time.sleep(.1)

