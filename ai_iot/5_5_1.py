import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
import time

def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode())

client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
client.on_message = on_message

broker_address = "192.168.137.116"

client.connect(broker_address)
client.subscribe("raspberry/data", qos=1)

client.loop_start()

try:
    while True:
        client.publish("esp8266/device1", "LED=0", qos=1)
        time.sleep(1)
        
        client.publish("esp8266/device1", "LED=100", qos=1)
        time.sleep(1)
        
        client.publish("esp8266/device1", "LED=255", qos=1)
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped")
    client.loop_stop()
    client.disconnect()

