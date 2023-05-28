// ej 12 ams eficiente, no se pueden usar floats lo que si
#include <stdio.h>

int main () {
	
	int x;
	
	printf ("ingrese un numero entre 1 y 4:  \n");
	scanf ("%i",&x);
	
	switch (x){
		
		case 1: printf ("lunes\n\n"); break; //case 2 significa si x es 2
		case 2: printf ("martes\n\n"); break;//el break sirve para terminar el switch
		case 3: printf ("miercoles\n\n"); break;//si no hay ningun break y ponemos 3, va a mostrar miercoles, jueves y numero erroneo
		case 4: printf ("jueves\n\n"); break;
		default: printf ("numero erroneo\n\n");
	}//no olvidar esta llave
		system ("pause");
		return 0;
	}
