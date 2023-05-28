#include <stdio.h>

int main (){
	int a, b, i;
	
	printf ("introdusca un numero: ");
	scanf ("%i", &a);
	
	/*printf ("introdusca un numero mayor al anterior: ");
	scanf ("%i", &b);
	
	while(a>=b){
	i++;
		printf ("introdusca un numero mayor al primero: ");
	scanf ("%i", &b);
	}*/
	
	//lo de arriba tambien se puede hacer con un do while, ambas formas están bien
	do{
		printf ("introdusca un numero mayor al primero: ");
        scanf ("%i", &b);	
	}
	while(b<a);//si b es menor a a se repite todo
	i++;

	
	
	for (i=a+1; i<b; i++){
		printf ("%i, ",i);
	}
	
	printf ("\n");
	
	system ("pause");
	return 0;
}
