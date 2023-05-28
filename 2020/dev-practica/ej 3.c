#include <stdio.h>
#define PI 3.1416
int main() {
	
	float p=PI, r, a;
	
	printf ("Introdusca el radio: ");
	scanf ("%f", &r);
	
	a=p*r*r;
	
	printf ("El area es de: %f",a);
	system ("pause");	
	return 0;
	
	
}
