import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
import threading

broker_address = "192.168.137.116"

def update_labels(temp, hum):
    temp_label.config(text=f"Temperature: {temp} °C")
    hum_label.config(text=f"Humidity: {hum} %")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    parts = message.split(",")
    if len(parts) == 3 and parts[0] == "device2":
        temperature = parts[1]
        humidity = parts[2]
        if root.winfo_exists():
            root.after(0, update_labels, temperature, humidity)

def mqtt_loop():
    client.loop_forever()

def set_led(value):
    value = int(value)
    message = f"LED={value}"
    client.publish("esp8266/device1", message, qos=1)

def on_closing():
    client.disconnect()
    root.destroy()

client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect(broker_address)
client.subscribe("raspberry/data", qos=1)

root = tk.Tk()
root.title("IoT Dashboard")
root.protocol("WM_DELETE_WINDOW", on_closing)

frame = ttk.Frame(root, padding=20)
frame.grid()

tk.Label(frame, text="LED Brightness (0~255):").grid(column=0, row=0, sticky="w")
slider = tk.Scale(frame, from_=0, to=255, orient="horizontal")
slider.set(0)
slider.grid(column=1, row=0, sticky="ew")

def slider_released(event):
    set_led(slider.get())

slider.bind("<ButtonRelease-1>", slider_released)

temp_label = ttk.Label(frame, text="Temperature: - °C")
temp_label.grid(column=0, row=1, columnspan=2, sticky="w", pady=10)

hum_label = ttk.Label(frame, text="Humidity: - %")
hum_label.grid(column=0, row=2, columnspan=2, sticky="w")

frame.columnconfigure(1, weight=1)

mqtt_thread = threading.Thread(target=mqtt_loop)
mqtt_thread.daemon = True
mqtt_thread.start()

root.mainloop()
