# -*- coding: utf-8 -*-
"""
[Neopixels RGB Micropython ESP8266] ===============================================================================

NEOPIXELS output to board 14 (digital)

Environment prepare:
In your Blynk App project:
    - add "ZERGBA" widget,
    - bind it to Virtual Pin V4 in merge mode
    - send on release as you want

    - Run the App (green triangle in the upper right corner).
    - define SSID and WiFi password that will be used by ESP8266 board
    - define your auth token for current example and run it

This started program will periodically call and execute event handler "write_virtual_pin_handler".
In app you can move push button that will cause LED switch on and will send virtual write event
to change LED state on blynk app.
=====================================================================================================================
"""
import blynklib_mp as blynklib
import network
import utime as time
from neopixel import NeoPixel
from machine import Pin

#Check Wifi Connexion
WIFI_SSID = 'NSI'
WIFI_PASS = 'touchard'
BLYNK_AUTH = '8ttqxxxxxxxxxxxxxxxxxxxxhYOKe4cg'

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
RGB_VPIN = 4

#This function is called at each smartphone request
@blynk.handle_event('write V{}'.format(RGB_VPIN))
def write_virtual_pin_handler(vpin, value):
    print("RGB",value)
    for n in range(0,4):
        np[n] = int(value[0]),int(value[1]),int(value[2])
    np.write()
    
while True:
    blynk.run()
    

