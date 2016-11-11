/*
  Combat Ready Light Show
  On the Arduino Uno
  by Jason Morris
*/

int fire[6];
#include "FunctionsUno.h"

void setup() {

//set the fire pins to output and turn them off
  for (int i = 0; i < 6; i++) {
    fire[i] = (i + 2);
    pinMode(fire[i], OUTPUT);
    digitalWrite(fire[i], LOW);
  }
  Serial.begin(9600);
}

void loop() {

//Once the serial command has been received, start the program
  if (Serial.available() > 0) {

    char letter = Serial.read();
    if (letter == '2') {
      
      wait(2600);
      steam(fire, 1);
      wait(3805);
      steam(fire, 1);
      wait(3860);
      steam(fire, 1);

      wait(5250);
      steam(fire, .75);

      wait(1100);
      musicnotes(fire, 400);
      musicnotes(fire, 400);
      musicnotes(fire, 400);
      musicnotes(fire, 400);

      intimidate(fire);
      wait(3330);
      intimidate(fire);
      wait(3370);
      intimidate(fire);
      wait(720);
      
      intimidate_rev(fire);
      wait(740);
      
      intimidate_half(fire);
      wait(6140);

      musicnotes(fire, 400);
      musicnotes(fire, 400);
      musicnotes(fire, 400);
      musicnotes(fire, 230);

      wait(50);
      intimidate_half(fire);
      wait(710);
      intimidate_half(fire);
      wait(733);
      intimidate_half(fire);
      wait(745);
      INTIMIDATE_FINAL(fire);
    }
  }
}
