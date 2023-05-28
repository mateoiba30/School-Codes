//condiciones multiples

#include <stdio.h>

int main () {
	
	int x;
	
	printf ("ingrese un numero: ");
	scanf ("%i",&x);
	
	if (x >= 1 || x <= 10)// ||=o (or)
	printf ("el numero %i es igual o mayor a 1 o el numero %i es menor o igual a 10 \n", x);
	else 
	printf ("el numero %i NO es igual o mayor a 1 o el numero no es menor o igual a 10 \n", x);
	
	system ("pause");
	return 0;
}
