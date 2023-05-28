int rojo=5;
int amarillo=2;
int verde=7;
int c=0;
/*ojo a partir del numero 30 en protoword, el celeste es para el negativo, la pata corta es la negativa, el cable negativo viene del pin GND
 * asignar el puerto siempre, 
*/
void setup() {
  pinMode(verde,OUTPUT);
  pinMode(amarillo,OUTPUT);
  pinMode(rojo,OUTPUT);
  Serial.begin(9600);
}
void loop() {
 digitalWrite(rojo,HIGH);
 delay(1000);
 digitalWrite(rojo,LOW);
 delay(1000);   
// digitalWrite(rojo,HIGH);
// delay(100);
// digitalWrite(rojo,LOW);
// delay(100);   
// digitalWrite(rojo,HIGH);
// delay(100);
// digitalWrite(rojo,LOW);
// delay(100);   
// digitalWrite(rojo,HIGH);
// delay(100);
// digitalWrite(rojo,LOW);
// delay(100);   
// digitalWrite(rojo,HIGH);
// delay(100);
// digitalWrite(rojo,LOW);
// delay(100);   
// digitalWrite(rojo,HIGH);
// delay(100);
// digitalWrite(rojo,LOW);
// delay(100);   
// digitalWrite(rojo,HIGH);
// delay(100);
// digitalWrite(rojo,LOW);
// delay(250);  
 
 digitalWrite(amarillo,HIGH);
 delay(1000);
 digitalWrite(amarillo,LOW);
 delay(1000); 
 
 digitalWrite(verde,HIGH);
 delay(1000);
 digitalWrite(verde,LOW);
 delay(1000);   
 
// digitalWrite(verde,HIGH);
// delay(100);
// digitalWrite(verde,LOW);
// delay(100);   
// digitalWrite(verde,HIGH);
// delay(100);
// digitalWrite(verde,LOW);
// delay(100);   
// digitalWrite(verde,HIGH);
// delay(100);
// digitalWrite(verde,LOW);
// delay(100);   
// digitalWrite(verde,HIGH);
// delay(100);
//  digitalWrite(verde,LOW);
// delay(100);   
// digitalWrite(verde,HIGH);
// delay(100);
// digitalWrite(verde,LOW);
// delay(100);   
// digitalWrite(verde,HIGH);
// delay(100);
// digitalWrite(verde,LOW);
// delay(250);  

 c++;
 Serial.println(c);
 if (c>=3){
   digitalWrite(rojo,LOW);
   digitalWrite(amarillo,LOW);
   digitalWrite(verde,LOW);
   delay(2000);
}
}
