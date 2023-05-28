#include <stdio.h>
#include <math.h>
int main() {
	// algoritmo de la burbuja
	int a,b,ax;
	
	printf ("ingrese el valor de a: ");
	scanf ("%i", &a);
   	printf ("ingrese el valor de b: ");
	scanf ("%i", &b);

ax=a;
a=b;
b=ax;
    
    printf ("el nuevo valor de a es de: %i \n",a);
    printf ("el nuevo valor de b es de: %i ",b);
	
	system ("pause");
	return 0;
}
