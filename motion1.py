from gpiozero import MotionSensor, LED
from signal import pause
from time import sleep

pir = MotionSensor(4)  
led = LED(14)    

while True:
     
     if pir.motion_detected:
         print("Motion!")
         led.on()
     else:
         print("no motion")
         led.off()

pause()

 

