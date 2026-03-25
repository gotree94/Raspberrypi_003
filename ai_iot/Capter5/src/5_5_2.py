import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
import time

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print("Received:", message)

    parts = message.split(",")
    if len(parts) == 3 and parts[0] == "device2":
        temperature = parts[1]
        humidity = parts[2]
        print("Temperature:", temperature)
        print("Humidity:", humidity)

client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
client.on_message = on_message

broker_address = "192.168.137.116"

client.connect(broker_address)
client.subscribe("raspberry/data", qos=1)

client.loop_start()

try:
    while True:
        pass

except KeyboardInterrupt:
    print("Stopped")
    client.loop_stop()
    client.disconnect()
