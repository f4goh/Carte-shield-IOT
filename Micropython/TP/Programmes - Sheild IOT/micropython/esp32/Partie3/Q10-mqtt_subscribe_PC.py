import paho.mqtt.client as mqtt

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client("python") #id must be unique
client.username_pw_set("touchard","MFmD747BIp8YIJYI") #login, password
client.on_message = on_message

client.connect("touchard.cloud.shiftr.io", 1883, 60)

client.subscribe("/capteurs/temperature")

while True:
    client.loop()
