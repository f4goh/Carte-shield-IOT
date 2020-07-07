# ESP8266 Clock


import network
import urequests
import ujson
import utime
from machine import Pin,I2C,RTC
from time import sleep
from ssd1306 import SSD1306_I2C

# user data
url = "http://worldtimeapi.org/api/timezone/Europe/Paris"

# initialization
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
rtc = RTC()


response = urequests.get(url)
    
if response.status_code == 200:    
    worldtime = ujson.loads(response.text)
    print(type(worldtime))
    print(worldtime.keys())
    print(worldtime)
    horloge = worldtime["datetime"]
    print(horloge)
    annee = int(horloge[0:4])
    mois = int(horloge[5:7])
    jour = int(horloge[8:10])
    heure = int(horloge[11:13])
    minute = int(horloge[14:16])
    seconde = int(horloge[17:19])
    subsecond = int(horloge[20:23])
    print(annee, mois, jour, heure, minute, seconde, subsecond)
    rtc.datetime((annee, mois, jour, 0,heure, minute, seconde, subsecond)) 
else:
    print("Pas de réponse")
    rtc.datetime((2019, 8, 2, 0,13,55, 0,0)) 
    
while True:
    horloge=rtc.datetime()
    heure= s =  "%02d" % horloge[4]+':'+"%02d" % horloge[5]+':'+"%02d" % horloge[6]
    oled.fill(0)
    oled.text(heure ,30, 40)
    oled.show()
    sleep(1)
    
    