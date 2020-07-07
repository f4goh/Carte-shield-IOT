from umqtt.robust import MQTTClient
import network
import sys
from machine import Pin

led = Pin(12,Pin.OUT)

# user data
ssid = "raspi-webgui" # wifi router name
pw = "touchardNSI" # wifi router password

def cb(topic, msg):
    print((topic, msg))
    valeur=int(msg.decode("ascii"))
    if valeur==1:
        led.on()
    elif valeur==0:
        led.off()

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)

# wait for connection
while not wifi.isconnected():
    pass

# wifi connected
print(wifi.ifconfig())

myMqttClient = b"micropython"

THINGSPEAK_URL = b"broker.shiftr.io"
THINGSPEAK_USER_ID = b'weatherSensors'
THINGSPEAK_MQTT_API_KEY = b'bme280Sensors'
client = MQTTClient(client_id=myMqttClient,
                    server=THINGSPEAK_URL,
                    user=THINGSPEAK_USER_ID,
                    password=THINGSPEAK_MQTT_API_KEY,
                    ssl=False)
client.set_callback(cb)

try:
    client.connect()
    print("connection ok");    
    client.subscribe("/actionneurs/led")
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()


while True:
    try:
        client.wait_msg()
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()
        print("exit")
