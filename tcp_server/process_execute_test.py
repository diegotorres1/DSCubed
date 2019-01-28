#hi
# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
LED = 23 # Broadcom pin 23 (P1 pin 16)
# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(LED, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(LED, GPIO.LOW)

class process_execute_test():
    def __init__(self):
        print('Process and Execute the commands')
    def pe_control(self,command):
        try:
            if (command == 3):
                GPIO.output(LED, GPIO.HIGH)
            else:
                GPIO.output(LED, GPIO.LOW)
        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            GPIO.cleanup() # cleanup all GPIO
