"""
analog read
"""
from machine import Pin, ADC
from time import sleep

adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)    # set 11dB input attentuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)

led = Pin(12,Pin.OUT)

while True:
    valeur=adc.read()    
    if valeur>401:
         led.on()
    else:
        led.off()
