#include<Arduino.h>

#define PIN1 26
#define PIN2 25
#define PIN3 33
#define PIN4 32
#define C4 262
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

  if(stepIndex >= 4){
    stepIndex = 0;
  }

}

// 音を鳴らす
// ----------------------
void playNote(int freq, int duration){

  if(freq == 0){
    delay(duration);
    return;
  }

  int delay_us = 1000000 / freq / 4;

  unsigned long start = millis();

  while(millis() - start < duration){

    stepMotor();

    delayMicroseconds(delay_us);
  }
}

void setup(){

  pinMode(PIN1, OUTPUT);
  pinMode(PIN2, OUTPUT);
  pinMode(PIN3, OUTPUT);
  pinMode(PIN4, OUTPUT);
}

void loop(){
	playNote(C4, 500);
}