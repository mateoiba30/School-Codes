#include <stdio.h>

int main() {
	
	int x, i, y;
	float  suma;
	
	printf ("introdece de cuantos numero quieres calcular la media: ");// no sabemos cunatos numeros va a ingresar el usuario
	scanf ("%i", &x);
	
	i=0;//si empieza al principio pones un cero
	while (i<x){
		printf ("introduce el numero %i: \n", i+1 );
		scanf ("%i", &y);
		i++;
		suma +=y;
	}
	
	suma/= x;
	
	printf ("el promedio es de : %f \n", suma);
	
	system ("pause");
	return 0;
}
