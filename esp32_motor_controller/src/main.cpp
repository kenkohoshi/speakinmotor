#include <WiFi.h>

const char* ssid = "C7-5F-TR";
const char* password = "robot20212021robot";

WiFiServer server(5000);

const int MOTOR_PIN = 5;

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();

}

void loop() {

  WiFiClient client = server.available();

  if (client) {

    Serial.println("Client connected");

    while (client.connected()) {

      if (client.available()) {

        String line = client.readStringUntil('\n');

        line.trim();

        int pwm = line.toInt();

        pwm = constrain(pwm, 0, 255);

        Serial.print("PWM = ");
        Serial.println(pwm);
      }
    }

    client.stop();

    Serial.println("Client disconnected");
  }
}