# -*- coding: utf-8 -*-
"""
[LDR Micropython ESP8266] ===============================================================================

Temperature sensor line to board 12 (onwewire conversion)

Environment prepare:
In your Blynk App project:
    - add "SuperChart" widget or other, and add datastream : name temperature
    - bind it to Virtual Pin V5
    - no update time menu (IOT send data periodically

    - Run the App (green triangle in the upper right corner).
    - define SSID and WiFi password that will be used by ESP8266 board
    - define your auth token for current example and run it

This started program send periodically (5s) with esp8266 timer temperature on superchart
and print the value on oled display
=====================================================================================================================
"""
import blynklib_mp as blynklib
from machine import Timer
import network
import utime as time
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms
import sys

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

#OLED and ds18s20 init
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
bus = OneWire(Pin(12))
ds = DS18X20(bus)
capteur_temperature = ds.scan()

#Timer init
tim = Timer(-1)

#Virtual Pin definition for Blynk interface
TEMP_VPIN = 5

#Interrupt handler executed every 5 seconds
def handleInterrupt(timer):
    ds.convert_temp()
    sleep_ms(750)
    temp_celsius = ds.read_temp(capteur_temperature[0])
    print("Température : ",temp_celsius)
    oled.fill(0)
    oled.text("temperature", 0, 0)
    oled.text(str(temp_celsius), 0, 20)
    oled.show()
    blynk.virtual_write(TEMP_VPIN, temp_celsius)

#Timer configuration
tim.init(period=5000, mode=Timer.PERIODIC, callback=handleInterrupt)

try:
    while True:
        blynk.run()
except KeyboardInterrupt:
    print('Ctrl-C pressed...exiting')
    tim.deinit()
    sys.exit()
