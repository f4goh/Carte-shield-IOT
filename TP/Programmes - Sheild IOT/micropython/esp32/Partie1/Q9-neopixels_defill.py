"""
Neopixels
       esp8266      esp32
broche   14(13)     18(13)
"""

NBPIXELS=4

from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

np = NeoPixel(Pin(18), NBPIXELS)


def defilement(color):
    for p in range(NBPIXELS):
        np[p] = color
        np[(p-1)%NBPIXELS]=(0,0,0)
        np.write()
        sleep_ms(100)

while(True):
    defilement((0,255,0))




