#include <Servo.h>
Servo servito;
int a=0;
void setup() {
  servito.attach(9);
  Serial.begin(9600);
}
void loop() {
  int x=analogRead(A0);
  int a=map(x, 0, 1023, 0, 180); //el mapeo redondea
 
  servito.write(a);
  Serial.print("Ángulo: ");
  Serial.println(a);
  delay(20);
}
