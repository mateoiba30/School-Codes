#include <stdio.h>// do while siem

int main(){
	
	int i;
	i=10;
	
/*	while (i<5){   //al ser falso esto no se ejecuta
		printf ("esto no se va a ejecutar nunca \n");
		i++;
	}
	*/
	
	do{
		printf ("esto se va a ejecutar al menos una vez \n");
		i++;//para que no se ejecute infinitas veces
	}while (i<15);  
		

	
	system ("pause");
	return 0;
}
