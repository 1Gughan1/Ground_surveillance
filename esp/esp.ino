#include <ESP32Servo.h>
const int servoPin = 13;
Servo myservo;

void setup() {
  Serial.begin(9600);
  myservo.attach(servoPin);
}

void loop() {
  if (Serial.available()) {
    int angle = Serial.parseInt(); 
    if (angle >= 0 && angle <= 180) {
      myservo.write(angle);
      delay(15);
      Serial.println("Servo moved to angle: " + String(angle));
    } else {
      Serial.println("Invalid angle. Please enter a value between 0 and 180.");
    }
  }
}
