"""
routines DMX
esp 8266 uart 1
esp 32   uart 2
        esp8266   esp32
broche   2(9)     17(4)
"""
from machine import Pin,I2C
from Dmx import Dmx
from time import sleep_ms
from Nunchuck import Nunchuck
import sys

#i2c = I2C(scl=Pin(22), sda=Pin(21))
i2c = I2C(scl=Pin(5), sda=Pin(4))
nun=Nunchuck(i2c)

#dmx=Dmx(17,2,16)  #ESP32 pin17,UART 2, 16 cannaux
dmx=Dmx(2,1,16)  #ESP8266 pin2,UART 1, 16 cannaux

try:
    while True:
        values=nun.read(1)
        print(values)
        dmx.setChannel(1,values[0])
        dmx.setChannel(2,values[1])
        dmx.setChannel(3,values[2])
        dmx.setChannel(4,values[3])
        sleep_ms(100)
        dmx.write()
except KeyboardInterrupt:
    print('Ctrl-C pressed...exiting')    
    sys.exit()

    
    




