#include <stdio.h>
#include <math.h>
int main() {
	
	int a,b,c,d,e,f;
	
printf ("introduzca el valor de a: ");
scanf ("%i", &a);

printf ("introduzca el valor de b: ");
scanf ("%i", &b);
	
    c= pow (a,b);
	printf ("la potencia es de: %i   \n",c);

    d=a+b;
    printf ("la suma es de: %i   \n",d);
    
    e=a%b;
    printf ("el resto es de: %i   \n",e);
    
    f=a/b;
    printf ("la division es de: %i ",f);

    	system ("pause");
	return 0;
}
