from machine import UART,Pin
from time import sleep_us
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
