#include<Arduino.h>
#include<motor.h>
void setup() {
}
void loop() {
  if (Serial.available()) {

    String line = Serial.readStringUntil('\n');
    int value = line.toInt();

    Serial.println(value); // デバッグ用

    if (value <= 0) return;

    setMotorSpeed(value);
  }
}