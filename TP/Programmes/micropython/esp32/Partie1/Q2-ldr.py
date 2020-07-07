"""
analog read  esp32
broche     35(A2)

ADC pins esp32: 0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 32, 33, 34, 35, 36, and 39.
"""

from machine import Pin, ADC
from time import sleep

adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)    # set 11dB input attentuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)

while True:
    valeur=adc.read()
    print(valeur)
    sleep(1)
   
  