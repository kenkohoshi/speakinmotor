#include <Arduino.h>
#include "motor.h"

// --------------------
// 初期化
// --------------------
void setup() {
  Serial.begin(115200);

  // モータ初期化（使ってるならここでpinModeなど）
  initMotor();  

  Serial.println("READY");  // PC側に開始合図
}

// --------------------
// メインループ
// --------------------
void loop() {

  if (Serial.available()) {

    // 1行受信（例: 440）
    String line = Serial.readStringUntil('\n');
    int value = line.toInt();

    // デバッグ
    Serial.println(value);

    // 無効値は無視
    if (value <= 0) return;

    // モータ駆動
    setMotorSpeed(value);
  }
}