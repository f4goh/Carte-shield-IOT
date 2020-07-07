"""
Neopixels
       esp8266      esp32
broche   14(13)     18(13)
"""
#couleur= (255, 255, 0)
from neopixel import NeoPixel
from machine import Pin

np = NeoPixel(Pin(14), 4)

for n in range(0,4):
    np[n] = couleur

np.write()

