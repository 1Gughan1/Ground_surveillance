#include <WiFi.h>

const char* ssid = "-(gughan)-";
const char* password = "gughan200";
WiFiServer server(5000);
int ledPin = 2;  // Pin connected to the LED
#define mot_1 13
#define mot_2 12
#define pwm 14
void setup() {
  Serial.begin(115200);
  delay(1000);

  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  pinMode(ledPin, OUTPUT);
  pinMode(mot_1, OUTPUT);
  pinMode(mot_2, OUTPUT);
  pinMode(pwm, OUTPUT);
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  
  if (client) {
    Serial.println("New client connected");
    
    while (client.connected()) {
      if (client.available()) {
        String receivedData = client.readStringUntil('\n');
        receivedData.trim();
        
        if (receivedData == "0") {
          digitalWrite(ledPin, LOW);
          digitalWrite(mot_1, LOW);
          digitalWrite(mot_2, LOW);
          analogWrite(pwm, 0);
          Serial.println("LED turned off");
        } else if (receivedData == "1") {
          digitalWrite(ledPin, HIGH);
          digitalWrite(mot_1, HIGH);
          digitalWrite(mot_2, LOW);
          analogWrite(pwm, 255);
          Serial.println("LED turned on");
        }
        else if (receivedData == "2") {
          digitalWrite(ledPin, HIGH);
          digitalWrite(mot_1, LOW);
          digitalWrite(mot_2, HIGH);
          analogWrite(pwm, 255);
          Serial.println("LED turned on");
      }
    }
    
    client.stop();
    Serial.println("Client disconnected");
  }
}
}
