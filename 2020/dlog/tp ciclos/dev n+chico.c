#include <stdio.h>
int main(){
	
	int val=0, min=0, i=0;
	
	printf("ingrese un valor: \n");
	scanf("%i", &min);
	
	for( i=1; i<=10; i++){
		
		printf("ingrese otro valor: \n");
		scanf("%i", &val);
		
		if(val<min)
		min=val;
	}
	printf("el menor numero es: %i \n", min);
	
	return 0;
	system ("pause");
}
