"""
routines DMX
esp 8266 uart 1
esp 32   uart 2
        esp8266   esp32
broche   2(9)     17(4)
"""
from machine import UART,Pin
from time import sleep_us,sleep_ms
from array import array

class Dmx():
    def __init__(self, pin, uart,nbChannels):
        self.pin = pin
        self.uart = uart
        self.buffer=array('B', [0] * nbChannels)

    def setChannel(self,channel,value):
        self.buffer[channel]=value

    def write(self):
        dmx_uart = Pin(self.pin, Pin.OUT)
        dmx_uart.value(0)
        sleep_us(74)
        dmx_uart.value(1)
        dmx_uart = UART(self.uart)
        dmx_uart.init(250000, bits=8, parity=None, stop=2)
        dmx_uart.write(self.buffer)
        del(dmx_uart)


dmx=Dmx(17,2,16)  #ESP32 pin17,UART 2, 16 cannaux
#dmx=Dmx(2,1,16)  #ESP8266 pin2,UART 1, 16 cannaux

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

