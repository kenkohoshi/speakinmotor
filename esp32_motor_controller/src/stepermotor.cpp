#include<Arduino.h>
#define PIN1 26
#define PIN2 25
#define PIN3 33
#define PIN4 32

int stepIndex = 0;

void stepMotor(){
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

  if (freq < 50) return;

  int delayTime = 1000000 / freq / 4;

  for (int i = 0; i < 10; i++) {
    stepMotor();
    delayMicroseconds(delayTime);
  }
}