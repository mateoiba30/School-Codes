#include <stdio.h>
int main () {
	
	int n=0, n2=0, c=0, i=0;
	
	for (i=1; i<=5; i++){
		
		printf("ingrese un numero: ");
		scanf("%i", &n);
		printf("ingrese un numero: ");
		scanf("%i", &n2);		
		
		if(n2<n)
		c++;
	}
	
	if(c>0)
	printf("el orden no es ascendente");
	else
	printf("el orden es ascendente");
	
	return 0;
}
