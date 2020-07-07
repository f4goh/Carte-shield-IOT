# Carte Shield IOT

La carte IOT au format Arduino UNO est un Shield qui se branche sans soudure aux microcontrôleurs ESP8266 ou ESP32. Cette carte est particulièrement adaptée pour le monde des objets connectés. 

Disponible chez [Crea-technologie](http://www.crea-technologie.com/index.php?product=120) 

- La carte Shield dispose des périphériques suivants :
- Écran OLED ;
- Capteur infrarouge pour télécommande RC5 ;
- Ruban de 4 DEL ;
- Capteur de température onewire ;
- Capteur de lumière LDR ;
- Connexion RS485 DMX ;
- Connexion pour passerelle UHF – LPWAN Sigfox (en cours) ;
- Connecteur I²C ;
- Exemples de programmes en Python et en C++;
- Trois séquences pédagogiques disponibles;
- Programmation avec [Thonny](https://thonny.org/)  ([Micropython](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html)) ou IDE Arduino (CPP).

Résumé des TP : [overview](https://github.com/f4goh/Carte-shield-IOT/blob/master/IOToverview.pdf) 

***

# Shield sur un ESP32

![ESP32](/images/esp32IOT.jpg  "Shield sur un ESP32")

***

# Shield et un ESP8266

![ESP8266](/images/esp8266IOT.jpg  "Shield sur un ESP8266")

Exemple de code Micropython

	"""
	Neopixels
	       esp8266      esp32
	broche   14(13)     18(13)
	"""
	   
	from neopixel import NeoPixel
	from machine import Pin
	
	np = NeoPixel(Pin(14), 4)
	
	np[0] = (255, 0, 0)
	np[1] = (0, 255, 0) 
	np[2] = (0, 0, 255)
	np[3] = (255, 255, 0)
	
	np.write()
	
***

# Accès Wifi avec un Raspberry PI

![IOT](/images/Wifi.png  "Iot et accès Wifi")
	
