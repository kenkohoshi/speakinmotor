#include <Arduino.h>

const int pin = 25;

void setup() {
  Serial.begin(115200);

  ledcSetup(0, 1000, 8);      // チャンネル0, 1kHz, 8bit
  ledcAttachPin(pin, 0);      // ピンとチャンネルを接続

  ledcWrite(0, 0);
}

void loop() {
  if (Serial.available()) {
    int freq = Serial.parseInt();

    if (freq > 0) {
      ledcSetup(0, freq, 8);
      ledcAttachPin(pin, 0);
      ledcWrite(0, 128);
    }
  }
}