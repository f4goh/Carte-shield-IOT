from umqtt.robust import MQTTClient
import network
import sys
import time
from time import sleep_ms
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20


sta_if = network.WLAN(network.STA_IF)
print(sta_if.active())
print(sta_if.ifconfig())

myMqttClient = b"micropython"

THINGSPEAK_URL = b"maqiatto.com"
THINGSPEAK_USER_ID = b'nsi.touchard@gmail.com'
THINGSPEAK_MQTT_API_KEY = b'xxxxxxxx'
client = MQTTClient(client_id=myMqttClient,
                    server=THINGSPEAK_URL,
                    user=THINGSPEAK_USER_ID,
                    password=THINGSPEAK_MQTT_API_KEY,
                    ssl=False)

try:
    client.connect()
    print("connection ok");
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()

bus = OneWire(Pin(12))
ds = DS18X20(bus)
capteur_temperature = ds.scan()

PUBLISH_PERIOD_IN_SEC = 10

while True:
    try:
        ds.convert_temp()       
        sleep_ms( 750 )
        temp_celsius = ds.read_temp(capteur_temperature[0])
        print("Température : ",temp_celsius )        
        client.publish("nsi.touchard@gmail.com/capteurs", str(int(temp_celsius)))
        print("publish ok");
        time.sleep(PUBLISH_PERIOD_IN_SEC)
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()
        print("exit")
