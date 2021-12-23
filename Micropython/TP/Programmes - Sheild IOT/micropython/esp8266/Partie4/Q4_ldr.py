# -*- coding: utf-8 -*-
"""
[LDR Micropython ESP8266] ===============================================================================

Ldr sensor line to board A0 (ADC - analog to digital conversion on dedicated pin)

Environment prepare:
In your Blynk App project:
    - add "Gauge" widget,
    - bind it to Virtual Pin V1
    - set name "Potentiometer"
    - set label /pin.##/
    - set update time=1 sec and assign 0-1024 values range to it


    - Run the App (green triangle in the upper right corner).
    - define SSID and WiFi password that will be used by ESP8266 board
    - define your auth token for current example and run it

This started program will periodically call and execute event handler "read_virtual_pin_handler".
that will try to get data from potentiometer and write it to related virtual pin.
Within App widget gauge value will be updated each 1 sec.
=====================================================================================================================
"""
import blynklib_mp as blynklib
import network
import utime as time
from machine import ADC,Pin,I2C
from ssd1306 import SSD1306_I2C

WIFI_SSID = 'NSI'
WIFI_PASS = 'touchard'
BLYNK_AUTH = '8ttqxxxxxxxxxxxxxxxxxxxxhYOKe4cg'

#Check Wifi Connexion
print("Connecting to WiFi network '{}'".format(WIFI_SSID))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('WiFi connect retry ...')
print('WiFi IP:', wifi.ifconfig()[0])

print("Connecting to Blynk server...")
blynk = blynklib.Blynk(BLYNK_AUTH,log=print)

#OLED and adc init
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
adc = ADC(0)

#Virtual Pin definition for Blynk interface
LDR_VPIN = 1

#Define 2 RGB colors
LOW_COLOR = '#f5b041'
HIGH_COLOR = '#85c1e9'



#This function is called at each smartphone request
@blynk.handle_event('read V{}'.format(LDR_VPIN))
def read_handler(vpin):
    ldr = adc.read()
    oled.fill(0)
    oled.text("ldr", 0, 0)
    oled.text(str(ldr), 0, 20)
    oled.show()
    print('ldr value=',ldr)
    if ldr<600:
        blynk.set_property(LDR_VPIN, 'color', LOW_COLOR)
    else:
        blynk.set_property(LDR_VPIN, 'color', HIGH_COLOR)
    blynk.virtual_write(vpin, ldr)



while True:
    blynk.run()
