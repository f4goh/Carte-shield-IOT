# -*- coding: utf-8 -*-
"""
[Led button Micropython ESP8266] ===============================================================================

Led output to board 0 (digital)

Environment prepare:
In your Blynk App project:
    - add "Button" widget,
    - bind it to Virtual Pin V2 in switch mode
    - add "LED" widget and assign Virtual Pin V3 to it

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

#LED init
led = Pin(0,Pin.OUT)

#Virtual Pin definition for Blynk interface
BUTTON_VPIN = 2
LED_VPIN = 3

#This function is called at each smartphone request
@blynk.handle_event('write V{}'.format(BUTTON_VPIN))
def write_virtual_pin_handler(vpin, value):
    print("pin",vpin,"value",value)
    if value[0]=='1':
        led.on()
        blynk.virtual_write(LED_VPIN,255)
    else:
        led.off()
        blynk.virtual_write(LED_VPIN,0)


while True:
    blynk.run()
