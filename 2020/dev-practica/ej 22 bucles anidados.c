#include <stdio.h>
//bucles anidados
//tablas de multiplicar del 1 al 9
int main (){
	int i, j;
	
	for(i=1; i<=9; i++){
		for(j=1; j<=10; j++){//tiene que decir que j=1 para que arranque en 1 y no (si es la tabla del 3) en 3//cuando el primer for dio una vuelta este dio 10
			printf ("%i x %i = %i \n", i, j, i*j);//se pueden hacer cuentas dentro de los printf
		}
		printf ("\n");//se pone fuera porque cada diez vueltas (1 tabla) frena
		system ("pause");//sirve para que todo se frene hasta que des una tecleada
	}

	
	system ("pause");
	return 0;
}
