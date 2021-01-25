from gpiozero import MotionSensor, LED
from time import sleep
from datetime import datetime
import smtplib
from email.message import EmailMessage
import pygame

pir = MotionSensor(4) # pir.when_motion = led.on # pir.when_motion = led.on
led = LED(14) 
sender = "donotreply1@csedge.org"
recipient= "paco@csedge.org"


def get_time():
    now = datetime.now()
    #date and time format: dd/mm/YYYY H:M:S
    format = "%d/%m/%Y %H:%M:%S"
    #format datetime using strftime() 
    time_formatted = now.strftime(format)
    
    return time_formatted

def send_email():
    
    time = get_time()
  
    body = "Intruder Alert  " + str(time)
    
    msg = EmailMessage()
    msg.set_content(body)
    
    msg['Subject'] = 'Alarm triggered'
    msg['From'] = sender
    msg['To'] = recipient
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("donotreply1@csedge.org", "codenext")
    
    #server.sendmail( "donotreply1@csedge.org", recipient, "Intruder alert" )
    server.send_message(msg)
    
    print("sending email...")
    
    server.quit()    
    
def play_sound():
    
    
    """
     sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0

    """
    
    pygame.init()
    pygame.mixer.init()
    #load the sound file
    mysound = pygame.mixer.Sound("siren.wav")

    #play the sound file for 10 seconds and then stop it
    mysound.play()
    sleep(10)
    mysound.stop()
 
    
    

def log_incident():
    
    time = get_time()
    with open('incidents.txt', 'a+') as f:    
        f.write(time)
        f.write("\n")
         
        print("incident logged")
        
 
while True:
    if pir.motion_detected:
        led.on()
        log_incident()
        #send_email()
        play_sound()
        sleep(4)
    else:
        print("no motion")
        led.off()

 

 