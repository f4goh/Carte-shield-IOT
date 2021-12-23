#ir 13

from machine import Pin
from time import sleep_us,ticks_us,ticks_diff
from neopixel import NeoPixel
import sys

ir = Pin(13, Pin.IN)
led = Pin(0,Pin.OUT)
np = NeoPixel(Pin(14), 4)


time_start=ticks_us()
code =2
actualBit=0
lastBit=1
bit=1
trigger=0

def callback(p):
    global time_start,code,actualBit,lastBit,bit,trigger
    edge=ir.value()
    time_stop=ticks_us()
    delta = ticks_diff(time_stop,time_start)
    time_start=time_stop
    if delta>2000:
        if bit==13:
            print ('-> ',code & 0x3f)
            trigger=code  & 0x3f
        code = 2
        lastBit=1
        actualBit=0
        bit=0
        led.value(led.value()^1)        
    else:        
        long=0
        valid=0
        if delta>1100:
            long=1        
        if edge==1:
            if lastBit==1:
                if long==1:
                    actualBit=0
                    lastBit=1
                    valid=1
            if lastBit==0:
                if long==0:
                    actualBit=0
                    lastBit=0
                    valid=1
        if edge==0:
            if lastBit==1:
                if long==0:
                    actualBit=1
                    lastBit=1
                    valid=1
            if lastBit==0:
                if long==1:
                    actualBit=1
                    lastBit=0
                    valid=1
        if valid==1:            
            bit+=1
            code|=actualBit
            if bit<13:
                code<<=1
            lastBit=actualBit
                    

ir.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)

couleur=(0,0,0)

try:
    while True:
        if trigger==1:
            couleur=(255,0,0)
        elif trigger==2:
            couleur=(0,255,0)
        elif trigger==3:
            couleur=(0,0,255)
        for n in range(0,4):
            np[n] = couleur
        np.write()
except KeyboardInterrupt:
    print('Ctrl-C pressed...exiting')
    ir.irq(trigger=0)
    sys.exit()



    
