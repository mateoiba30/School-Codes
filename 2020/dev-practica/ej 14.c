//condiciones multiples

#include <stdio.h>

int main () {
	
	int x;
	
	printf ("ingrese un numero: ");
	scanf ("%i",&x);
	
	if (x >= 1 && x <= 10)// &&=y (and)
	printf ("el numero %i esta entre 1 y 10 \n", x);
	else 
	printf ("el numero %i NO esta entre 1 y 10 \n", x);
	
	system ("pause");
	return 0;
	
	
	
	
}
