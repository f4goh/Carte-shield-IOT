"""
test les prerphériques de la carte (hors infra rouge) en mode automatique
"""
NBPIXELS=4
INTENSITE=8
HAUTEUR=64-7

from time import sleep,sleep_ms
from onewire import OneWire
from ds18x20 import DS18X20
from machine import Pin,I2C,ADC
from ssd1306 import SSD1306_I2C
from neopixel import NeoPixel
from time import sleep_ms

import sys

np = NeoPixel(Pin(14), NBPIXELS)
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
bus = OneWire(Pin(12))



#Clignote la led 10 fois

def led():
    led = Pin(0,Pin.OUT)

    for n in range(10):
        print("led",n)
        led.on()
        sleep_ms(300)
        led.off()
        sleep_ms(300)

#Lire le capteur ldr 10 fois
def ldr():
    adc = ADC(0)

    for n in range(10):
        valeur=adc.read()    
        print("ldr",n,valeur)
        sleep(1)
    
#Defiler les leds de couleur
def un_defilement(color):
    for p in range(NBPIXELS):
        np[p] = color
        np[(p-1)%NBPIXELS]=(0,0,0)
        np.write()
        sleep_ms(100)        

def defiler_couleurs():
    un_defilement((0,INTENSITE,0))
    un_defilement((INTENSITE,0,0))
    un_defilement((INTENSITE,INTENSITE,0))
    un_defilement((0,INTENSITE,INTENSITE))
    un_defilement((0,INTENSITE,0))
    un_defilement((INTENSITE,INTENSITE,INTENSITE))
    np[3]=(0,0,0)
    np.write()

#Defiler un texte sur l'écran oled
def scroll_texte():
    for h in range(0,HAUTEUR):
        oled.fill(0)
        oled.text("Hello NSI", 30, h)
        oled.show()
    for h in range(HAUTEUR,0,-1):
        oled.fill(0)
        oled.text("Hello NSI", 30, h)
        oled.show()

#Mesurer 20 temperatures avec affichage sur l'écran oled        
def temperature():
    ds = DS18X20(bus)
    capteur_temperature = ds.scan()
    for n in range(20):
        ds.convert_temp()       
        sleep_ms(750)
        temp_celsius = ds.read_temp(capteur_temperature[0])
        print("Température : ",temp_celsius )
        oled.fill(0)
        oled.text("temperature", 0, 0)
        oled.text(str(temp_celsius), 0, 20)
        oled.show()

print("IOT test automatique")
print("--------------------")
print("1: Clignoter la led 10 fois")
led()
print("2: Lire le capteur de lumière ldr 10 fois")
ldr()
print("3: Defiler les leds de couleur")
defiler_couleurs()
print("4: Defiler un texte sur l'écran oled")
scroll_texte()
print("5: Mesurer 20 temperatures avec affichage sur l'écran oled")
temperature()
print("Au revoir")


