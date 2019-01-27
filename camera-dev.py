from picamera import PiCamera
from gpiozero import LED
from time import sleep

led = LED(2)

cam = PiCamera()
cam.resolution = (2000,2000)
cam.rotation = 270
led.on()
cam.start_preview()
sleep(2)
cam.capture('test.jpg')
cam.close()
led.off()
