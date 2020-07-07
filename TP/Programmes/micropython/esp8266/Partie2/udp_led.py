from machine import Pin
#import usocket as socket
import socket

led = Pin(0,Pin.OUT)

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
