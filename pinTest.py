import RPi.GPIO as GPIO
import time

#GPIO Basic initialization
GPIO.setmode(GPIO.BOARD) # <- Use the physical pin numbering
GPIO.setwarnings(False)

# Use a variable for the Pin to use
# Use the pin number that correspponds to the GPIO pin
led = 13
#Initialize your pin
GPIO.setup(led,GPIO.OUT)

#Turn on the LED
print("LED on")
GPIO.output(led,1)

#Wait 5s
time.sleep(1)

#Turn off the LED
print("LED off")
GPIO.output(led,0)