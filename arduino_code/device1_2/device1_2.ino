#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* device_name = "device1";
const char* ssid = "jmc";
const char* password = "123456789";
const char* mqtt_server = "192.168.137.148";

WiFiClient espClient;
PubSubClient client(espClient);

const int RED_PIN = D13;
const int GREEN_PIN = D12;
const int BLUE_PIN = D11;

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void setWhiteBrightness(int brightness) {
  analogWrite(RED_PIN, brightness);
  analogWrite(GREEN_PIN, brightness);
  analogWrite(BLUE_PIN, brightness);
}

void callback(char* topic, byte* payload, unsigned int length) {
  String msg;
  for (unsigned int i = 0; i < length; i++) {
    msg += (char)payload[i];
  }

  Serial.println("subscribe: " + msg);

  if (msg.startsWith("LED=")) {
    int value = msg.substring(4).toInt();
    value = constrain(value, 0, 255);
    setWhiteBrightness(value);

    String response = "OK LED=" + String(value);
    client.publish("raspberry/data", response.c_str());
    Serial.println("Publish: " + response);
  }
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

  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);

  analogWriteRange(255); 
  setWhiteBrightness(0);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
