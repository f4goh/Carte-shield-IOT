import picoweb
from machine import Pin
import usocket as socket
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms
import network


bus = OneWire(Pin(19))
ds = DS18X20(bus)
capteur_temperature = ds.scan()

# user data
ssid = "Livebox-0E00" # wifi router name
pw = "FzhSJGFouVGNLYKAMa" # wifi router password

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)

# wait for connection
while not wifi.isconnected():
    pass

# wifi connected
print(wifi.ifconfig())

 
app = picoweb.WebApp(__name__)


def web_page():
    html = """<html>
            <head>
            <title>ESP neopixels Web Server</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script>
 
            setInterval(function() {
            getData();
            }, 5000); //mise à jour toutes les 5000 milli Secondes 
 
            function getData() {
               var xhttp = new XMLHttpRequest();
               xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                       document.getElementById("TEMPValue").innerHTML = this.responseText;
                   }
               };
             xhttp.open("GET", "TEMPValue", true);
             xhttp.send();
            }
            </script>
            </head>
            <body>
            <h1>Température de la pièce: <span id="TEMPValue">"""+str(conversion_temerature())+"""</span> °C
            </h1> 
            </body>
            </html>"""

    return html

def conversion_temerature():
    ds.convert_temp()       
    temp_celsius = ds.read_temp(capteur_temperature[0])
    print("Température : ",temp_celsius )
    return temp_celsius
    

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(web_page())

@app.route("/TEMPValue")
def index(req, resp):    
    yield from picoweb.start_response(resp)
    yield from resp.awrite(str(conversion_temerature()))


app.run(debug=True, port=80, host = wifi.ifconfig()[0])
