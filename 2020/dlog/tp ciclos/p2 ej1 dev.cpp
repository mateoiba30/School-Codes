#include <iostream>

int main (){
	
	int l=0, d=0, t=0;
	
	for(d=1; d<=30; d++){
		
		printf("ingrese la cantidad de L/m2 precipitados en el dia %i \n", d);
		scanf("%i", &l);
		
		t+=l;
	}
	printf("los L/m2 de lluvia de Junio fueron de: %i\n", t);
	
	system("pause");
}
