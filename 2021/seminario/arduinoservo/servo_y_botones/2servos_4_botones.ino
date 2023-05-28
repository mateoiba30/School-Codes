//IZUIERDA  DERECHA  ARRIBA  ABAJO
//SERVO1                    SERVO2

//declaramos la librería
#include <Servo.h>

//declaramos los servos
Servo servito1;
Servo servito2;

//declaramos más variables
int h=0;//angulos de cada servo
int v=0;
//pines de los botones, no hace falta ponerlos como variables
int iz=2;//blanco
int de=4;//negro
int ar=6;//naranja
int ab=8;//verde

int s1=10;//pines de los servos, no hace falta ponerlos como variables
int s2=11;

int btn_iz=0;
int btn_de=0;
int btn_ar=0;
int btn_ab=0;

void setup() {
  servito1.attach(s1);//primer servo: eje horizontal. declaro el pin del servo
  pinMode(iz, INPUT);
  pinMode(de, INPUT);//input significa que son de entrada (manda  info y no muestra nada)
  
  servito2.attach(s2);//segundo servo eje vertical. declaro el pin del servo
  pinMode(ar, INPUT);
  pinMode(ab, INPUT);
}

void loop() {//esto es lo que se ejecuta (el loop es como un while
  
  //decimos el pin de cada botón
  btn_iz=digitalRead(iz);
  btn_de=digitalRead(de);
  btn_ar=digitalRead(ar);
  btn_ab=digitalRead(ab);

  //cada boton mueve uno de los servos
  if(btn_de==HIGH){
    h=h+5;
    delay(20);}//los delays sirven para que no se mueva tan rápido
  if(btn_iz==HIGH){
    h=h-5;
    delay(20);}
  if(btn_ar==HIGH){
    v=v+5;
    delay(20);}
  if(btn_ab==HIGH){
    v=v-5;
    delay(20);}
    
  //los servos toman los valores de las variables
  servito1.write(h);
  servito2.write(v);
  delay(20);//retraso el loop
}
