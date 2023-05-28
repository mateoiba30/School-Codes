#include <stdio.h>

int main() {
	
	int n1,n2,n3,mx,mm;
	
	printf ("ingrese un numero: ");
	scanf ("%i", &n1);
	printf ("ingrese un numero: ");
	scanf ("%i", &n2);
	printf ("ingrese un numero: ");
	scanf ("%i", &n3);
	
	if (n1>n2)
    	if (n1>n3)	   
	    mx=n1;	  
	    else
		mx=n3;
	   
	else
	    if (n2>n3)
	    mx=n2;
	    else
	    mx=n3;
	    
	    
	    
	    
	if (n1<n2)
    	if (n1<n3)	   
	    mm=n1;	  
	    else
		mm=n3;
	   
	else
	    if (n2<n3)
	    mm=n2;
	    else
	    mm=n3;


	printf ("el mayor numero es: %i \n", mx)  ;  
	printf ("el menor numero es: %i \n", mm)  ; 
	    system ("pause");
	    return 0;
	}
	
			

