# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client("python") #id must be unique
client.username_pw_set("weatherSensors","bme280Sensors") #login, password
client.on_message = on_message

client.connect("broker.shiftr.io", 1883, 60)

client.subscribe("/sensors/temperature")

while True:
    client.loop()
