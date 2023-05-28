#include <stdio.h>
#include <math.h>
int main() {
	
	int a,b;
	
	a=10;
	b=2;
	
    a= pow (a,b);
	printf ("la potencia es de: %i   \n",a);

   a += b;
    printf ("la suma es de: %i   \n",a);
    
    a%=b;
    printf ("el resto es de: %i   \n",a);
    
    a/=b;
    printf ("la division es de: %i \n",a); 
    
    a++;
    printf ("a +1 es de: %i \n",a);
    
       a--;
    printf ("a -1 es de: %i ",a);//resultados en cadena
	
		system ("pause");
	return 0;
}
