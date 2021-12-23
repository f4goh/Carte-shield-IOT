"""
wifi connexion
"""

import network

# user data
ssid = "raspi-webgui" # wifi router name
pw = "touchardNSI" # wifi router password

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)

# wait for connection
while not wifi.isconnected():
    pass

# wifi connected
print(wifi.ifconfig())
    