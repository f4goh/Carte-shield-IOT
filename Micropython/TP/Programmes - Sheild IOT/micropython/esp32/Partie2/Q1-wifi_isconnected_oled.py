"""
wifi connexion
"""

import network
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import ubinascii

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)

i2c = I2C(scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)

# wifi is connected ?
if wifi.isconnected():
    ip=wifi.ifconfig()
    oled.text(ip[0] ,10, 40)
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    #oled.text(mac ,10, 50)
else:
    oled.text("not connected" ,10, 40)
oled.show()




