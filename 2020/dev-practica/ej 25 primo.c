#include <stdio.h>
int main (){

	int n, i, s=0, r;
	
	printf ("ingrese un numero: ");
	scanf ("%i", &n);
	
	for(i=2; i<n; i++){//no lo divido por uno ni por el mismo número porque
	r = n % i ;

	if (r==0)
    s=1;//no se acumula,  si juna vez o mil veces r=0 s siempre va a ser =1
	}
    
    if (s==1)
   	printf ("%i NO es un numero primo \n", n);
	else
	printf ("%i es un numero primo \n", n);
		
    system ("pause");
    return 0;
}
