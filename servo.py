# testing servo control with pwm gpio output

from gpiozero import Servo
from time import sleep

servo = Servo(13,min_pulse_width=0.001,max_pulse_width=0.002)

servo.min()
