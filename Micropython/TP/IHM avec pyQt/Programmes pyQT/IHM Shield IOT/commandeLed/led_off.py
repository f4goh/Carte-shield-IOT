from machine import Pin
from time import sleep_ms

#led = Pin(0,Pin.OUT)
led = Pin(12,Pin.OUT)

led.off()
print("led off")

    