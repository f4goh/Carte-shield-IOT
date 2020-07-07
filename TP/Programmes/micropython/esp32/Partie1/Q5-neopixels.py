"""
Neopixels
       esp8266      esp32
broche   14(13)     18(13)
"""
   
from neopixel import NeoPixel
from machine import Pin

np = NeoPixel(Pin(18), 4)

np[0] = (0, 255, 255) # set to red, full brightness
np[1] = (0, 128, 0) # set to green, half brightness
np[2] = (0, 0, 64)
np[3] = (64, 0, 64)
np.write()

