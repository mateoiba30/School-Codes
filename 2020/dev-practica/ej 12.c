// ej 11 mas eficiente

#include <stdio.h>

int main () {
	
	int x;
	
	printf ("ingrese un numero entre 1 y 4:  \n");
	scanf ("%i",&x);
	
	if (x==1)

	   printf ("lunes\n\n");
	else if (x==2)
	    printf ("martes\n\n");
    else if (x==3)
	     printf ("miercoles\n\n");
	else if ( x==4)
	 printf ("jueves\n\n");
	 	else 
	 printf ("numero incorrecto\n\n");
	 
	 system ("pause");
	 return 0;
}
