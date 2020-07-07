"""
oled defill haut bas
"""
   
HAUTEUR=64-7

from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)


while True:
    for h in range(0,HAUTEUR):
        oled.fill(0)
        oled.text("Hello NSI", 30, h)
        oled.show()
    for h in range(HAUTEUR,0,-1):
        oled.fill(0)
        oled.text("Hello NSI", 30, h)
        oled.show()
        
    
