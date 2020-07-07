import paho.mqtt.client as mqtt

client = mqtt.Client("python") #id must be unique
client.username_pw_set("weatherSensors","bme280Sensors") #login, password

client.connect("broker.shiftr.io", 1883, 60)

while True:
    #client.loop()
    valeur=input("saisir l'etat de la led 0/1 ?")
    client.publish("/actionneurs/led", valeur)
	
