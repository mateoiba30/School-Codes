
#include <Servo.h>
Servo servito;
int a=0;
int x=4;
int y=2;
int botonazul=0;
int botonamarillo=0;

void setup() {
  servito.attach(10);
  Serial.begin(9600);
  pinMode(x, INPUT);
  pinMode(y, INPUT);
}

void loop() {
  botonazul=digitalRead(x);
  botonamarillo=digitalRead(y);
  
  if(botonazul==HIGH){
    a=a+5;
    delay(20);}
  if(botonamarillo==HIGH){
    a=a-5;
    delay(20);}
     
  servito.write(a);
  Serial.print("Ángulo: ");
  Serial.println(a);
  delay(20);
}
