#include <stdio.h>

int main() {
	int x;
	float y;
	float r;
	
	printf ("Ingrese el valor de x: ");
	scanf ("&i",&x);
	
	printf ("Ingrese el valor de y: ");
	scanf ("&f",&y);
	
	r=x*y;
	
	printf ("el resultado es de: %f.\n", r);
	system ("pause");	
	return 0;
}
