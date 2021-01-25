# motion_gpio
Raspberry pi examples using GPIO Zero and motion sensor (PIR). 

## Supplies
1. Raspberry Pi 3 or 4
2. 1 LED
3. 220Ω or 330Ω resistor
4. PIR motion sensor HC-SR501 - 5V
5. M-F Jumper wires

## motion1.py
A detects motion with PIR sensor and logs the change. It also turns on an LED connected to GPIO pin 14. 

## motion2.py
A Raspberry Pi Alarm. It Detects motion and turns on LED, sends email, stores a time stamp in a text file and plays a .wav file using the ***pygame*** library. It also uses ***smtplib*** to send email.

#### setting up email:
Before running this project, make sure to set up a gmail account. 

### installing Pygame:
````bash
sudo apt-get update
python3 -m pip install -U pygame --user
````
if lib2


### wiring
!['fritzing diagram'](https://i.imgur.com/MTdryvE.png)

