
"""This simple py dedicate the way to control led and make it blink.
@author Find Hao
@time 2015.12.18
"""
import RPi.GPIO as GPIO
import time


LED = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
try:
    while 1:
        GPIO.output(LED,1)
        time.sleep(1)
        GPIO.output(LED,0)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()