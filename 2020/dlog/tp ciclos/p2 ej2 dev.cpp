#include <iostream>

int main(){
	
	int t=0, p=0, i=0;
	
	for (i=1; i<=20; i++){
		printf ("ingrese el dinero aportado por el amigo %i \n", i);
		scanf("%i", &p);
		
		t+=p;
	}
	if (t>10000)
	printf ("alcanza para un viaje \n");
	else
	printf ("alcanza para un equipo de cine hogareno\n");
	
	system ("pause");
}
