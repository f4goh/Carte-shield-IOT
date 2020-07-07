

couleur= (0, 255, 0, 255)

from machine import UART
import machine, time
from array import array

dmx = array('B', [0] * 16)




def write_frame():
    #led = machine.Pin(0,machine.Pin.OUT)    
    dmx_uart = machine.Pin(2, machine.Pin.OUT)
    dmx_uart.value(0)
    time.sleep_us(74)
    dmx_uart.value(1)
    # Now turn into a UART port and send DMX data
    dmx_uart = UART(1)
    dmx_uart.init(250000, bits=8, parity=None, stop=2)
    #send bytes
    dmx_uart.write(dmx)
    #Delete as its going to change anyway
    del(dmx_uart)

for n in range(0,4):
    dmx[n+1]=couleur[n]

write_frame()

