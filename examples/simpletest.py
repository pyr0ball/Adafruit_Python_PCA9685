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
led_max = 32  # Max pulse length out of 4095
led_half = int(led_max/2)
led_quart = int(led_max/4)

#------------- Function originally for servo --------------#
# Helper function to make setting a servo pulse width simpler.
#def set_servo_pulse(channel, pulse):
#	pulse_length = 1000000		# 1,000,000 us per second
#	pulse_length //= 60		# 60 Hz
#	print('{0}us per period'.format(pulse_length))
#	pulse_length //= 4096		# 12 bits of resolution
#	print('{0}us per bit'.format(pulse_length))
#	pulse *= 1000
#	pulse //= pulse_length
#	pwm0.set_pwm(channel, 0, pulse)

# Set frequency to 960hz, good for eyes.
pwm0.set_pwm_freq(960)

print('Simple color phase on RGB LED, bus 0, channels 0-2 , press Ctrl-C to quit...')
while True:
	# Move servo on channel O between extremes.
	# PWM syntax: pwm[bus].set_pwm([channel], [off state], [on state])
	# Example: pwm0.set_pwm(0, 0, 4095)
	pwm0.set_pwm(0, 0, led_max)
	pwm0.set_pwm(1, 0, led_half)
	pwm0.set_pwm(2, 0, led_quart)
	pwm0.set_pwm(3, 0, led_max)
	time.sleep(0.1)
	pwm0.set_pwm(0, 0, led_half)
	pwm0.set_pwm(1, 0, led_max)
	pwm0.set_pwm(2, 0, led_half)
	pwm0.set_pwm(3, 0, led_min)
	time.sleep(0.1)
	pwm0.set_pwm(0, 0, led_quart)
	pwm0.set_pwm(1, 0, led_half)
	pwm0.set_pwm(2, 0, led_max)
	pwm0.set_pwm(3, 0, led_quart)
	time.sleep(0.1)
	pwm0.set_pwm(0, 0, led_half)
	pwm0.set_pwm(1, 0, led_quart)
	pwm0.set_pwm(2, 0, led_half)
	pwm0.set_pwm(3, 0, led_half)
	time.sleep(0.1)
