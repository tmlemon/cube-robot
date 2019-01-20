from picamera import PiCamera
from time import sleep

cam = PiCamera()
cam.resolution = (2000,2000)
cam.rotation = 180
cam.start_preview()
sleep(2)
cam.capture('o.jpg')
cam.close()
