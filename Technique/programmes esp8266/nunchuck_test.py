"""
Nunchuck I2C
"""

from machine import Pin,I2C
from time import sleep_ms
from Nunchuck import Nunchuck
import sys

i2c = I2C(scl=Pin(5), sda=Pin(4))

nun=Nunchuck(i2c)

try:
    while True:
        print(nun.read(0))
        sleep_ms(500)
except KeyboardInterrupt:
    print('Ctrl-C pressed...exiting')    
    sys.exit()



