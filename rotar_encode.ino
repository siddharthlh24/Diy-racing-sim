
#include <Encoder.h>

#include <ButtonDebounce.h>

String p1=",";
Encoder myEnc(5, 6);
//ButtonDebounce button(4, 250);


int b1 =0;
int acc=0;
int brk = 0;
void setup() {
  Serial.begin(9600);
  pinMode(2,INPUT_PULLUP);
  pinMode(A0,INPUT);
  pinMode(A2,INPUT);
}


long oldPosition  = -999;

void loop() {
  long newPosition = myEnc.read();
  if (newPosition != oldPosition) {
    oldPosition = newPosition;
  
  }
    //button.update();
    //b1 = int(button.state());
    
    b1=!digitalRead(2);
    brk=analogRead(A0);
    acc=analogRead(A2);
    
    //Serial.print(newPosition);
    //Serial.print(",");
    Serial.println(newPosition+p1+b1+p1+brk+p1+acc);
}
