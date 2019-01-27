# 2019-01-27
# tring out gpio header control with in Python

from gpiozero import LED
from time import sleep

led = LED(2)

led.on()
sleep(10)
led.off()
