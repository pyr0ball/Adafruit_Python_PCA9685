# Simple demo of of the PCA9685 PWM servo/LED controller library.
# Author: Tony DiCola
# Modified for RGB LED drive by Alan Weinstock 5/2/2017
# License: Public Domain
# For further information about the PCA9685 chip, please see the below links:
# https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf
# https://media.readthedocs.org/pdf/micropython-pca9685/latest/micropython-pca9685.pdf

from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm0 = Adafruit_PCA9685.PCA9685()

# Initialize next serial bus address:
# Each successive address will be called by it's individual designation set by the below variables.
# The datasheet linked in at the top of this script has a diagram on how to set the i2c address jumpers.
# the example below assumes the same i2c bus is being used in daisychain
# Syntax: pwm[index] = Adafruit_PCA9685.PCA9685(address=0x[hardware i2c bits], busnum=[i2c bus index]
#pwm0 = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
#pwm1 = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)
#pwm2 = Adafruit_PCA9685.PCA9685(address=0x42, busnum=1)


# Configure min and max LED pulse lengths
led_min = 0  # Min pulse length out of 4095
led_max = 256  # Max pulse length out of 4095
led_half = int(led_max/2)
led_quart = int(led_max/4)

# Configure pulse lengths based on 256 steps for easy RGB conversion
rgb_pwm = int(led_max/256)

# Set up easily readable variables for RGB color channels

#-- Panel 0 --#
red0 = 0
green0 = 1
blue0 = 2
white0 = 3

#-- Panel 1 --#
red1 = 4
green1 = 5
blue1 = 6
white1 = 7

#-- Panel 2 --#
red2 = 8
green2 = 9
blue2 = 10
white2 = 11

#-- Panel 3 --#
red3 = 12
green3 = 13
blue3 = 14
white3 = 15


# Set frequency to 960hz, easy on the eyes.
pwm0.set_pwm_freq(960)

print('Simple color phase on RGB LED, bus 0, channels 0-2 , press Ctrl-C to quit...')
while True:
	
	# PWM syntax: pwm[bus].set_pwm([channel], [off state], [on state])
	# Example: pwm0.set_pwm(0, 0, int(rgb_pwm*256))
	pwm0.set_pwm(red0, 0, rgb_pwm*183)
	pwm0.set_pwm(green0, 0, rgb_pwm*210)
	pwm0.set_pwm(blue0, 0, rgb_pwm*255)
#	time.sleep(0.1)
#	pwm0.set_pwm(red0, 0, led_half)
#	pwm0.set_pwm(green0, 0, led_max)
#	pwm0.set_pwm(blue0, 0, led_half)
#	time.sleep(0.1)
#	pwm0.set_pwm(red0, 0, led_quart)
#	pwm0.set_pwm(green0, 0, led_half)
#	pwm0.set_pwm(blue0, 0, led_max)
#	time.sleep(0.1)
#	pwm0.set_pwm(red0, 0, led_half)
#	pwm0.set_pwm(green0, 0, led_quart)
#	pwm0.set_pwm(blue0, 0, led_half)
#	time.sleep(0.1)
