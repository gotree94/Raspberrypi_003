#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* device_name = "device1";
const char* ssid = "iot";
const char* password = "123456789";
const char* mqtt_server = "192.168.137.116";

WiFiClient espClient;
PubSubClient client(espClient);

unsigned long lastSendTime = 0;
int count = 0;

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  String msg;
  for (int i = 0; i < length; i++) {
    msg += (char)payload[i];
  }

  Serial.println("subscribe: " + msg);
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect(device_name)) {
      client.subscribe("esp8266/device1");
    } else {
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(9600);
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
  if (now - lastSendTime > 1000) {
    lastSendTime = now;
    String msg = "device1:" + String(count++);
    client.publish("raspberry/data", msg.c_str());
    Serial.println("Published: " + msg);
  }
}
