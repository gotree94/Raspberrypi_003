import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
import time

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
client.on_message = on_message

broker_address="192.168.137.116"
client.connect(broker_address)
client.subscribe("pc",1)

client.loop_forever()