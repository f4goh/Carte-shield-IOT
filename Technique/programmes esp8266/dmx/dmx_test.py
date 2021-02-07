"""
routines DMX
esp 8266 uart 1
esp 32   uart 2
        esp8266   esp32
broche   2(9)     17(4)
"""
from Dmx import Dmx
from time import sleep_ms

#dmx=Dmx(17,2,16)  #ESP32 pin17,UART 2, 16 cannaux
dmx=Dmx(2,1,16)  #ESP8266 pin2,UART 1, 16 cannaux

dmx.setChannel(1,0)
dmx.setChannel(2,0)
dmx.setChannel(3,0)
dmx.setChannel(4,255)
dmx.write()


for n in range(0,255):
    dmx.setChannel(1,n)
    dmx.setChannel(2,255-n)
    dmx.setChannel(3,255-n)
    sleep_ms(10)
    dmx.write()

