#include "DHT.h"

#define DHTPIN D8
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

unsigned long lastReadTime = 0;
const unsigned long readInterval = 2000;

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  unsigned long now = millis();

  if (now - lastReadTime >= readInterval) {
    lastReadTime = now;

    float h = dht.readHumidity();
    float t = dht.readTemperature();

    if (!isnan(h) || !isnan(t)) {
      Serial.print("Humidity: ");
      Serial.print(h);
      Serial.print("%  Temperature: ");
      Serial.print(t);
      Serial.println("°C ");
    }
  }
}
