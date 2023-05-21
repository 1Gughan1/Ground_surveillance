#include <WiFi.h>

const char* ssid = "-(gughan)-";
const char* password = "gughan200";
WiFiServer server(5000);
#define ledpin 2
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

  pinMode(ledpin,OUTPUT);
  
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
          turnOffLed();
        } else if (receivedData == "1") {
          turnOnLed();
        }
      }
    }
    
    client.stop();
    Serial.println("Client disconnected");
  }
}

void turnOnLed() {
  // Code to turn on the LED
  Serial.println("LED turned on");
  digitalWrite(ledpin, HIGH);
}

void turnOffLed() {
  // Code to turn off the LED
  Serial.println("LED turned off");
  digitalWrite(ledpin, LOW);
}
