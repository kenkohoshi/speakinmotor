#include <WiFi.h>

const char* ssid = "C7-5F-TR";
const char* password = "robot20212021robot";

WiFiServer server(5000);

String buffer = "";

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  server.begin();
  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("Client connected");

    while (client.connected()) {
      while (client.available()) {
        char c = client.read();

        // 改行で1行として扱う
        if (c == '\n') {
          Serial.println(buffer); // ここでデータ確定
          buffer = "";
        } else {
          buffer += c;
        }
      }
    }

    client.stop();
    Serial.println("Client disconnected");
  }
}