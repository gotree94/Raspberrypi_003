import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
import time

broker_address="192.168.137.116"
client = mqtt.Client(client_id="ClientPub",callback_api_version=CallbackAPIVersion.VERSION2)

client.connect(broker_address)

count = 0
try:
    while True:
        count = count + 1
        client.publish("hello", str(count))
        print(count)
        time.sleep(1.0)
    
except KeyboardInterrupt:
    pass


