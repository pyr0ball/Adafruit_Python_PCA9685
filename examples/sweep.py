# Simple demo of of the PCA9685 PWM servo/LED controller library.
# Author: Tony DiCola
# Modified for RGB LED drive by Alan Weinstock 5/2/2017
# License: Public Domain
# For further information about the PCA9685 chip, please see the below links:
# https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf
# https://media.readthedocs.org/pdf/micropython-pca9685/latest/micropython-pca9685.pdf

# Usage: 
# python rgb_control.py [i2c index] [i2c address in decimal] [PWM channel] [red] [green] [blue] [white] [brightness percent]

from __future__ import division
import time
import sys
import threading
import random


# Import the PCA9685 module.
import Adafruit_PCA9685 as PCA9685

pwm_ch = 0

#-- Panel 0 --#
if pwm_ch == 0:
	R = 0
	G = 1
	B = 2
	W = 3

#-- Panel 1 --#
if pwm_ch == 1:
	R = 4
	G = 5
	B = 6
	W = 7

#-- Panel 2 --#
if pwm_ch == 2:
	R = 8
	G = 9
	B = 10
	W = 11

#-- Panel 3 --#
if pwm_ch == 3:
	R = 12
	G = 13
	B = 14
	W = 15

# Configure min and max LED pulse lengths
led_min = 0  # Min pulse length out of 4095
led_max = 128  # Max pulse length out of 4095
#led_brightness = int((int(bright)/100) * led_max) # Apply brightness percentage to max pulse length

#def initialize_gpio()
pwm = PCA9685.PCA9685()

def color_test(channel, frequency, speed, step):
	p = pwm(channel, 0, frequency)
	p.start(0)
	while True:
		for dutyCycle in range(0, 101, step):
			p.ChangeDutyCycle(dutyCycle)
			time.sleep(speed)
		for dutyCycle in range(100, -1, -step):
			p.ChangeDutyCycle(dutyCycle)
			time.sleep(speed)

def color_test_thread():
	threads = []
	threads.append(threading.Thread(target=color_test, args=(R, led_max, 0.02, 5)))
	threads.append(threading.Thread(target=color_test, args=(G, led_max, 0.035, 5)))
	threads.append(threading.Thread(target=color_test, args=(B, led_max, 0.045, 5)))
	for t in threads:
		t.daemon = True
		t.start()
	for t in threads:
		t.join()

def main():  
    try:
        #initialize_gpio()
        print("\nPress ^C (control-C) to exit the program.\n")
        color_test_thread()
    except KeyboardInterrupt:
        pass
#    finally:
#        GPIO.cleanup()

if __name__ == '__main__':  
    main()

# Create variables from command line arguments
#i2c_index = sys.argv[1]
#dec_address = sys.argv[2]
#hex_address = int(dec_address) + 64
#address = "%x" % hex_address
#pwm_ch = int(sys.argv[3])
#red = int(sys.argv[4])
#gre = int(sys.argv[5])
#blu = int(sys.argv[6])
#whi = int(sys.argv[7])
#bright = sys.argv[8]

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
#pwm0 = Adafruit_PCA9685.PCA9685()

# Initialize next serial bus address:
# Each successive address will be called by it's individual designation set by the below variables.
# The datasheet linked in at the top of this script has a diagram on how to set the i2c address jumpers.
# the example below assumes the same i2c bus is being used in daisychain
# Syntax: pwm[index] = Adafruit_PCA9685.PCA9685(address=0x[hardware i2c bits], busnum=[i2c bus index]
#pwm = Adafruit_PCA9685.PCA9685(busnum=1)
#pwm1 = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)
#pwm2 = Adafruit_PCA9685.PCA9685(address=0x42, busnum=1)


# Configure pulse lengths based on 256 steps for easy RGB conversion
#rgb_pwm = int(led_brightness/256)

# Set up easily readable variables for RGB color channels

# Set frequency to 960hz, easy on the eyes.
#pwm.set_pwm_freq(960)
	
	# PWM syntax: pwm[bus].set_pwm([channel], [off state], [on state])
	# Example: pwm0.set_pwm(0, 0, int(rgb_pwm*255))
#pwm.set_pwm(redl, 0, rgb_pwm*red)
#pwm.set_pwm(green, 0, rgb_pwm*gre)
#pwm.set_pwm(blue, 0, rgb_pwm*blu)
#pwm.set_pwm(white, 0, rgb_pwm*whi)
