#!/usr/bin/env python
import RPi.GPIO as GPIO

xPin = 0

def setup():
  GPIO.setmode(GPIO.BOARD)    # Numbers GPIOs by physical location
  GPIO.setup(xPin, GPIO.OUT)
  
	p = GPIO.PWM(xPin, 1000)    # set Frequece to 1KHz
	p.start(0)                    # Duty Cycle = 0
  
  #
  # Loop - WIP
  #
  
def destroy():
	GPIO.output(xPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
