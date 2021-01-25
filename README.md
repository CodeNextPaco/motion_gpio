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
A Raspberry Pi Alarm. It Detects motion and turns on LED, sends email, stores a time stamp in a text file and plays a .wav file using the **pygame** library. It also uses **smtplib** to send email.

#### setting up email:
Before running this project, make sure to set up a Gmail account. It is recommended that you create a new account for development purposes, mainly because you will need to lower the security of the Gmail account in order to send emails from 3rd party apps like the Pi.

Once you create a new Gmail account and have logged on, you have to allow Less Secure Apps in the [Gmail Settings](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4N6zWFHhA4gF-QIN2rc4STkrg9-4IRTuyZh_sDTSVr707HuxQnbHAr2qqWQZP5oc47S7EEDFVG0DgFR58hQJm7w2xClvg). 

Change the sender email and password in your code.

### installing Pygame:
````bash
$ sudo apt-get update
$ python3 -m pip install -U pygame --user
````

If you run the program and you get an error referencing libsdl2, use this command to update your pygame library.
````bash
$ sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0

````

### wiring
!['fritzing diagram'](https://i.imgur.com/MTdryvE.png)

