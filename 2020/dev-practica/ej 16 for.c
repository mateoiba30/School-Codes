#include <stdio.h>
 int main() {

    int  x, y, i;
     
	printf ("indruduce un numero: ");
	scanf ("%i",&x);
	printf("indruduce un numero mayor al anterior: ");
	scanf("%i",&y);	
	
	
	
    for (i=x + 1 ; i < y ; i++){//cunado empiez; condicion que si es falsa se frena todo; incremento
        printf ("%i, ", i);// no va aspersant NUNCA//muestra el valor de i ( el cual cambia +1 con cada repetición
    }
    printf ("\n");
 
 
    i= x+1;//arriba se pone cuando empieza 
    while (i<y){//solo se usa la condicion
	  printf ("%i, ",i);
	  i++;//acá se pone de a cuanto avanza
	//equivalente al for
	

	}
		 printf ("\n");
    system ("pause");
	return 0;
}
