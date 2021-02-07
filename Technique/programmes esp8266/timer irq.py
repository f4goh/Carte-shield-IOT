"""
timer irq (Ctrl-C pressed...exiting)
"""

from machine import Timer
from machine import Pin
import sys
tim = Timer(-1)

led = Pin(0, mode=Pin.OUT) # enable GP16 as output to drive the LED

ledState=0

def handleInterrupt(timer):
    global ledState
    ledState^=1
    led.value(ledState)


#tim.init(period=1000, mode=Timer.ONE_SHOT, callback=tick)
tim.init(period=500, mode=Timer.PERIODIC, callback=handleInterrupt)

try:
    while True:
        pass
except KeyboardInterrupt:
    print('Ctrl-C pressed...exiting')
    tim.deinit()
    sys.exit()
