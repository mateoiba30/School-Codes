/* un sensor lee la temperatura cada hora de 8 a 12hs, durante 5 dìas de la semana. Calcular y mostrar:
a-la mayor temperatura de cada dìa
b-la mayor temperaturadela semana
c-l dìa y la hora de mayor temperatura
*/
#include<iostream>
#include <stdio.h>
using namespace std;
int main() {
	
	int matriz[5][5];
	int cd=0, ch=0;
	float a=0, b=0;
	
	for(int d=0; d<5; d++){
	for(int h=0; h<5; h++){
		cout<<"Temperatura del dia "<<d+1<<" , a las  "<<h+8<<" horas en grados celcius: "<<endl;
		cin>>matriz[d][h]; 
	}
}
	for(int d=0; d<5; d++){
	a=0;
	for(int h=0; h<5; h++){
		if(matriz[d][h]>a)
		a=matriz[d][h];
		
		if(matriz[d][h]>b){
		b=matriz[d][h];
		cd=d;
		ch=h;}
	}
		cout<<"La mayor temperatura del dia "<<d+1<<" es de: "<<a<<" C"<<endl;
		
	}
	    cout<<"La mayor temperatura de la semana es de: "<<b<<" C, y fue el dia "<<cd+1<<" a las "<<ch+8<<" horas"<<endl;
	return 0;
}
