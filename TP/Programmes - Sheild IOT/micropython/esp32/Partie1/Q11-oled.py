"""
oled test
"""
   

from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(22), sda=Pin(21))

oled = SSD1306_I2C(128, 64, i2c, 0x3c)
oled.fill(0)
oled.text("Hello NSI", 30, 30)
oled.show()
    
