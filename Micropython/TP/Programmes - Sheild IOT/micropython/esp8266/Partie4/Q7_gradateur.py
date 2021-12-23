# -*- coding: utf-8 -*-
"""
[Neopixels RGB Micropython ESP8266] ===============================================================================

NEOPIXELS output to board 14 (digital)

Environment prepare:
In your Blynk App project:
    - add "Slider" widget,
    - bind it to Virtual Pin V6 with send release off write interval 100ms
    - min value : 0, max value 128
    

    - Run the App (green triangle in the upper right corner).
    - define SSID and WiFi password that will be used by ESP8266 board
    - define your auth token for current example and run it

This started program will periodically call and execute event handler "write_virtual_pin_handler".
In app you can move slider to increase or decrase neopixels light power
=====================================================================================================================
"""
import blynklib_mp as blynklib
import network
import utime as time
from neopixel import NeoPixel
from machine import Pin



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

#Neopixels init
np = NeoPixel(Pin(14), 4)

#Virtual Pin definition for Blynk interface
LEVEL_VPIN = 6

def update_neopixels(level):
    for n in range(0,4):
        color = level,0,level
        np[n] = color
    np.write()
    
@blynk.handle_event('write V{}'.format(LEVEL_VPIN))
def write_virtual_pin_handler(vpin, value):
    global level
    print("Level",value[0])
    level=int(value[0])
    update_neopixels(level)
    
while True:
    blynk.run()
    

