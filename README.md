# This is a useability expansion on the Adafruit Python PCA9685 library
## Adafruit Python PCA9685
Python code to use the PCA9685 PWM servo/LED controller with a Raspberry Pi or BeagleBone black.

## Installation

To install the library from source (recommended) run the following commands on a Raspberry Pi or other Debian-based OS system:

    sudo apt-get install git build-essential python-dev
    cd ~
    git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
    cd Adafruit_Python_PCA9685
    sudo python setup.py install

Alternatively you can install from pip with:

    sudo pip install adafruit-pca9685

Note that the pip install method **won't** install the example code.

### New additions:

There are two new example scripts, and more complete set of explainations in the scripts.

`simpletest.py` - phases between 1/4, 1/2 and full brightness on each channel (R, G, B) in order at 10hz

`colorspectrum.py` - allows you to set RGB color using 0-255 RGB format

`rgb_control.py` - designed to be called by an external application (or terminal) using arguments

Syntax: `rgb_control.py [i2c index] [i2c address in decimal] [PWM channel] [red] [green] [blue] [white] [brightness percent]`

Example:

`python rgb_control.py 1 0 0 255 255 255 255 100`

The above example sets all four PWM channels (RGBW) to full color and brightness on i2c bus 1, PWM controller 0 (0x40)

### Parameters for rgb_control (i2c parameters are listed for Raspberry Pi. Other platforms may differ)

 - i2c_index: 0,1 (default is 1)
 - i2c_address: 0-64 (default is 0, script handles conversion to hex and offset)
 - PWM_Channel: 0-3 (default is 0, Each PCA9685 handles up to 4 complete RGBW channels)
 - red: 0-255 (red channel color level based on 256 levels)
 - green: 0-255 (green channel color level based on 256 levels)
 - blue: 0-255 (blue channel color level based on 256 levels)
 - white: 0-255 (white channel color level based on 256 levels)
 - brightness: 1-100 (brightness level based on percentage)
