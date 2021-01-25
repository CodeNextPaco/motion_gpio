from gpiozero import MotionSensor, LED
from signal import pause
from time import sleep

pir = MotionSensor(4) # pir.when_motion = led.on # pir.when_motion = led.on
led = LED(14)    
 
 

while True:
     led.on()
     if pir.motion_detected:
         print("Motion!")
     else:
         print("no motion")

pause()

 

