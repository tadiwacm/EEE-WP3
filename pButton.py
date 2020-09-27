#Pushbutton Code
#MDZTAD004

import  RPi.GPIO as GPIO
import time

#choose pin setup
GPIO.setmode(GPIO.BOARD)

#supress warnings
GPIO.setwarnings(False)

#setup the inputs and output pins
#set up the pin for the button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#setup the pin for the LED
GPIO.setup(18, GPIO.OUT)



def main():

 print("LED on")
 GPIO.output(18, GPIO.HIGH)
######delay for 1 millisecond#####
 time.sleep(1)
 print("LED off")
 GPIO.output(18,GPIO.LOW)

#####button pressed#####
 try:
  while True:
   button_state = GPIO.input(16);
   if button_state ==  False:
    GPIO.output(18, True)
    print('Button Pressed. LED on.')
#sleep for 0.6 milliseconds
    time.sleep(.6)
   else:
    GPIO.output(18, False)
     except:
  GPIO.cleanup()

if __name__ == '__main__':
 main()




