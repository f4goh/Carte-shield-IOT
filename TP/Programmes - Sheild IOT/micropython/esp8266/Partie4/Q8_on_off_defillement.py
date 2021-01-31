# -*- coding: utf-8 -*-
"""
[Neopixels RGB Micropython ESP8266] ===============================================================================

NEOPIXELS output to board 14 (digital)

Environment prepare:
In your Blynk App project:
    - add "Button" widget,
    - bind it to Virtual Pin V2 in switch mode

    - Run the App (green triangle in the upper right corner).
    - define SSID and WiFi password that will be used by ESP8266 board
    - define your auth token for current example and run it

This started program will call and execute event handler "write_virtual_pin_handler" when button is pushed
In app you can enable or disable leds scan.
=====================================================================================================================
"""
import blynklib_mp as blynklib
import network
import utime as time
from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms


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
NBPIXELS=4
np = NeoPixel(Pin(14), 4)

#Virtual Pin definition for Blynk interface
BUTTON_VPIN = 2
#leds scrolling state
etat=0

@blynk.handle_event('write V{}'.format(BUTTON_VPIN))
def write_virtual_pin_handler(vpin, value):
    global etat
    print("pin",vpin,"value",value)
    etat=int(value[0])
        
def defilement(color):
    for p in range(NBPIXELS):
        np[p] = color
        np[(p-1)%NBPIXELS]=(0,0,0)
        np.write()
        sleep_ms(100)

def stop():
    for p in range(NBPIXELS):
        np[p] = (0,0,0)
    np.write()

while True:
    blynk.run()
    if etat==1:
        defilement((0,255,0))
    else:
        stop()

    
    

