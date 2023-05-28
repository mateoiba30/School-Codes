// arrays=vector= estructura de datos que acumula má de un valor (puedo recuperar esos valores)
#include <stdio.h>
// #include <iostream> el "string" solo funciona con el iostream, y se complica con el uso del "printf"
using namespace std;
int main (){
	
	int goles[5]={0, 0, 0, 0, 0} ;//variable con 5 valores    {0, 0, 0, 0, 0}= inicializo cada lugar desde cero porque la primera posición es cero
	/* si son 500 goles hacer:
	for (i=0; i<500; i++)
	goles[i]=0;
	*/
	int suma=0, mejores=0, i=0;
	float prom=0;
//	string nombre[5]={"mateo", "sabina", "aleajndro", "sonia ", "michi"};  //string es para cadena de texto
	
	for (i=0; i<5; i++) //no es menor o igual porque el cero ya es una posición (0, 1, 2, 3, 4)
	{
		printf("ingrese los goles de %i: \n", i+1); //saco el ", nombre[i]"
		scanf("%i", & goles[i]);
		
		suma=suma+goles[i];	
	}
	printf("el equipo anoto %i goles\n", suma);
	prom=suma/5;

	for ( i=0; i<5; i++){
		if(goles[i]>prom)
		mejores++;
	}
	
	printf("los jugadores que superan el promedio de %f goles es de: %i \n", prom, mejores);
	
	
	
	return 0;
	
}
