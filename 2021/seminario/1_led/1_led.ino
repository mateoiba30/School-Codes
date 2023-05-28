int verde=6;
//tiene que ser un pion pwm para poder mostrar distintas intensidades
void setup() {
  pinMode(verde,OUTPUT); 
  // put your setup code here, to run once:

}

void loop() {
   analogWrite(verde,10);
   delay(1000);
   analogWrite(verde,60);
   delay(1000);
   analogWrite(verde,110);
   delay(1000); 
   analogWrite(verde,160);
   delay(1000);
   analogWrite(verde,210);
   delay(1000);
   analogWrite(verde,260);
   delay(1000);
   analogWrite(verde,310);
   delay(1000);
  // put your main code here, to run repeatedly:

}
