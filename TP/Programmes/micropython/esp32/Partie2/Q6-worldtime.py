# ESP32 Clock
import network
import urequests
import ujson
import utime

# user data
ssid = "raspi-webgui" # wifi router name
pw = "touchardNSI" # wifi router password

# user data
url = "http://worldtimeapi.org/api/timezone/Europe/Paris"

# initialization

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)

# wait for connection
while not wifi.isconnected():
    pass

# wifi connected
print(wifi.ifconfig())

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
    
else:
    print("Pas de réponse")
    
#2019-08-02T19:41:32.781620
"""

"""

    