//function definitions

//wait function instead of delay so that the entire show can easily be
//slowed down or sped up. ex: change to delay(timenum*2) to go twice as slow
void wait(int timenum) {
  delay(timenum);
}





//sequence that makes fire leds look like steam
void steam(int fire[6], int Speed) {

  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], HIGH);
    wait(21);
  }

  wait(1220 * Speed);

  for (int i = 5; i > -1; i--) {
    digitalWrite(fire[i], LOW);
    wait(25);
  }
}



//do the musical notes on the fire leds
void musicnotes(int fire[6], int ltime) {
  digitalWrite(fire[5], HIGH);
  wait(160);
  digitalWrite(fire[5], LOW);
  digitalWrite(fire[2], HIGH);
  wait(320);
  digitalWrite(fire[2], LOW);
  digitalWrite(fire[5], HIGH);
  wait(160);
  digitalWrite(fire[5], LOW);
  digitalWrite(fire[2], HIGH);
  wait(320);
  digitalWrite(fire[2], LOW);
  digitalWrite(fire[4], HIGH);
  wait(160);
  digitalWrite(fire[4], LOW);
  digitalWrite(fire[1], HIGH);
  wait(320);
  digitalWrite(fire[1], LOW);
  digitalWrite(fire[5], HIGH);
  wait(160);
  digitalWrite(fire[5], LOW);
  digitalWrite(fire[2], HIGH);
  wait(320);
  digitalWrite(fire[2], LOW);
  digitalWrite(fire[5], HIGH);
  wait(160);
  digitalWrite(fire[5], LOW);
  digitalWrite(fire[2], HIGH);
  wait(160);
  digitalWrite(fire[2], LOW);
  digitalWrite(fire[0], HIGH);
  wait(424);
  digitalWrite(fire[0], LOW);
  digitalWrite(fire[1], HIGH);
  wait(160);
  digitalWrite(fire[1], LOW);
  digitalWrite(fire[5], HIGH);
  wait(320);
  digitalWrite(fire[5], LOW);
  digitalWrite(fire[3], HIGH);
  wait(160);
  digitalWrite(fire[3], LOW);
  digitalWrite(fire[0], HIGH);
  wait(320);
  digitalWrite(fire[0], LOW);
  digitalWrite(fire[1], HIGH);
  wait(160);
  digitalWrite(fire[1], LOW);
  digitalWrite(fire[5], HIGH);
  wait(320);
  digitalWrite(fire[5], LOW);
  digitalWrite(fire[3], HIGH);
  wait(160);
  digitalWrite(fire[3], LOW);
  digitalWrite(fire[0], HIGH);
  wait(320);
  digitalWrite(fire[0], LOW);
  digitalWrite(fire[4], HIGH);
  wait(160);
  digitalWrite(fire[4], LOW);
  digitalWrite(fire[2], HIGH);
  wait(160);
  digitalWrite(fire[2], LOW);
  digitalWrite(fire[0], HIGH);
  wait(ltime);
  digitalWrite(fire[0], LOW);
}





//intimidate part on fire leds
void intimidate(int fire[6]) {
  digitalWrite(fire[0], HIGH);
  wait(175);
  digitalWrite(fire[0], LOW);
  digitalWrite(fire[1], HIGH);
  wait(350);
  digitalWrite(fire[1], LOW);
  digitalWrite(fire[2], HIGH);
  wait(175);
  digitalWrite(fire[2], LOW);
  wait(275);
  digitalWrite(fire[3], HIGH);
  wait(175);
  digitalWrite(fire[3], LOW);
  digitalWrite(fire[4], HIGH);
  wait(350);
  digitalWrite(fire[4], LOW);
  digitalWrite(fire[5], HIGH);
  wait(450);
  digitalWrite(fire[5], LOW);
}





//reverse intimidate on fire leds
void intimidate_rev(int fire[6]) {
  digitalWrite(fire[5], HIGH);
  wait(175);
  digitalWrite(fire[5], LOW);
  digitalWrite(fire[4], HIGH);
  wait(350);
  digitalWrite(fire[4], LOW);
  digitalWrite(fire[3], HIGH);
  wait(175);
  digitalWrite(fire[3], LOW);
  wait(275);
  digitalWrite(fire[2], HIGH);
  wait(175);
  digitalWrite(fire[2], LOW);
  digitalWrite(fire[1], HIGH);
  wait(350);
  digitalWrite(fire[1], LOW);
  digitalWrite(fire[0], HIGH);
  wait(450);
  digitalWrite(fire[0], LOW);
}





//half intimidate on fire leds
void intimidate_half(int fire[6]) {
  digitalWrite(fire[0], HIGH);
  digitalWrite(fire[1], HIGH);
  digitalWrite(fire[2], HIGH);
  wait(95);
  digitalWrite(fire[0], LOW);
  digitalWrite(fire[1], LOW);
  digitalWrite(fire[2], LOW);
  wait(80);
  digitalWrite(fire[0], HIGH);
  digitalWrite(fire[1], HIGH);
  digitalWrite(fire[2], HIGH);
  wait(270);
  digitalWrite(fire[0], LOW);
  digitalWrite(fire[1], LOW);
  digitalWrite(fire[2], LOW);
  wait(80);
  digitalWrite(fire[0], HIGH);
  digitalWrite(fire[1], HIGH);
  digitalWrite(fire[2], HIGH);
  wait(125);
  digitalWrite(fire[0], LOW);
  digitalWrite(fire[1], LOW);
  digitalWrite(fire[2], LOW);
  wait(325);
  digitalWrite(fire[3], HIGH);
  digitalWrite(fire[4], HIGH);
  digitalWrite(fire[5], HIGH);
  wait(95);
  digitalWrite(fire[3], LOW);
  digitalWrite(fire[4], LOW);
  digitalWrite(fire[5], LOW);
  wait(80);
  digitalWrite(fire[3], HIGH);
  digitalWrite(fire[4], HIGH);
  digitalWrite(fire[5], HIGH);
  wait(270);
  digitalWrite(fire[3], LOW);
  digitalWrite(fire[4], LOW);
  digitalWrite(fire[5], LOW);
  wait(80);
  digitalWrite(fire[3], HIGH);
  digitalWrite(fire[4], HIGH);
  digitalWrite(fire[5], HIGH);
  wait(450);
  digitalWrite(fire[3], LOW);
  digitalWrite(fire[4], LOW);
  digitalWrite(fire[5], LOW);
}






//final intiidate on all fire leds
void INTIMIDATE_FINAL(int fire[6]) {
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], HIGH);
  }
  wait(95);
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], LOW);
  }
  wait(80);
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], HIGH);
  }
  wait(270);
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], LOW);
  }
  wait(80);
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], HIGH);
  }
  wait(125);
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], LOW);
  }
  wait(325);
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], HIGH);
  }
  wait(95);
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], LOW);
  }
  wait(80);
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], HIGH);
  }
  //wait(270);
  wait(850);
  for (int i = 0; i < 6; i++) {
    digitalWrite(fire[i], LOW);
  }
}

