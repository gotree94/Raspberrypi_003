#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

#define DHTPIN D8
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

const char* device_name = "device2";
const char* ssid = "jmc";
const char* password = "123456789";
const char* mqtt_server = "192.168.137.148";

WiFiClient espClient;
PubSubClient client(espClient);

unsigned long lastSendTime = 0;
const unsigned long interval = 2000;

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect(device_name)) {
      client.subscribe("esp8266/device2");
    } else {
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(9600);
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  unsigned long now = millis();
  if (now - lastSendTime >= interval) {
    lastSendTime = now;

    float temp = dht.readTemperature();
    float hum = dht.readHumidity();

    if (!isnan(temp) && !isnan(hum)) {
      String payload = "device2," + String(temp, 1) + "," + String(hum, 1);
      client.publish("raspberry/data", payload.c_str());
      Serial.println("Published: " + payload);
    }
  }
}
