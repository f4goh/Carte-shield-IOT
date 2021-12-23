from machine import Pin
#import usocket as socket
import socket,sys
import network

led = Pin(12,Pin.OUT)

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


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 5000))
print("A l'écoute du port 5000")
while True:
    data, addr = s.recvfrom(1024)
    print('received:',data,'from',addr)
    if (data.decode()=='o'):
        led.on()
    elif (data.decode()=='n'):
        led.off()
    elif (data.decode()=='q'):
        s.close()
        sys.exit()
