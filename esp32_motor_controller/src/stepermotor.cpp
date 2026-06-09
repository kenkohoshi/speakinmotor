#include <Arduino.h>
#include "motor.h"

// ピン（ULN2003 / 28BYJ-48想定）
#define PIN1 26
#define PIN2 25
#define PIN3 33
#define PIN4 32

int stepIndex = 0;

void initMotor() {
  pinMode(PIN1, OUTPUT);
  pinMode(PIN2, OUTPUT);
  pinMode(PIN3, OUTPUT);
  pinMode(PIN4, OUTPUT);
}

void stepMotor() {

  digitalWrite(PIN1, LOW);
  digitalWrite(PIN2, LOW);
  digitalWrite(PIN3, LOW);
  digitalWrite(PIN4, LOW);

  switch(stepIndex){
    case 0: digitalWrite(PIN1, HIGH); break;
    case 1: digitalWrite(PIN2, HIGH); break;
    case 2: digitalWrite(PIN3, HIGH); break;
    case 3: digitalWrite(PIN4, HIGH); break;
  }

  stepIndex++;
  if(stepIndex >= 4) stepIndex = 0;
}

void setMotorSpeed(int freq) {

  if (freq < 50) return;   // ノイズカット

  int delayTime = 1000000 / freq / 4;

  for (int i = 0; i < 10; i++) {
    stepMotor();
    delayMicroseconds(delayTime);
  }
}