

#couleur= (255, 0, 0, 255)

from Dmx import Dmx

dmx=Dmx(17,2,16)  #ESP32 pin17,UART 2, 16 cannaux
#dmx=Dmx(2,1,16)  #ESP8266 pin2,UART 1, 16 cannaux

for n in range(0,4):
    dmx.setChannel(n+1,couleur[n])

dmx.write()

