#include <BluetoothSerial.h>

BluetoothSerial SerialBT;

#include <ESP32Servo.h>

Servo servo1;

#define LED_PIN 2

void setup() {
  SerialBT.begin("ESP32-Bluetooth");
  pinMode(LED_PIN, OUTPUT);
  servo1.attach(13);
  Serial.begin(9600);
}

void loop() {
  Serial.println(SerialBT.read());
  
  if (SerialBT.available()) {
    char c = SerialBT.read();
    if (c == '1') {
      digitalWrite(LED_PIN, HIGH);
      servo1.write(180);
      SerialBT.println("LED ON");
    } else if (c == '0') {
      digitalWrite(LED_PIN, LOW);
      servo1.write(0);
      SerialBT.println("LED OFF");
    }
  }
}
