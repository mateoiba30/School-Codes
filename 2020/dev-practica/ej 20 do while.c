#include <stdio.h>

int main() {
	
	int i;
	char l;
	
	do{//el mensaje de que ingrese una letra es doble porque usamos un char
		printf ("ingresa una letra: ");
		fflush (stdin);//para que el mensaje no sea doble
		scanf ("%c", &l);//es una c porque es de char
	}
	while(l!='s' && l!='S');//el o (||) no funciona porque si una es falsa todo es falsa//si es distinto a s o S se hara el proceso
	i++;//hasta acá es parte del while
	
	printf ("letra correcta \n");

	
	system ("pause");
	return 0;
}
