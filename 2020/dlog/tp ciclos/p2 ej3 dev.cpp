#include <iostream>
int main (){
	
	int i=0, p1=0, p2=0, t1=0, t2=0, j=0;
	char e1[25], e2[25];
	
	printf ("ingrese el nombre del equipo 1: ");
	scanf("%s", &e1);
	printf ("ingrese el nombre del equipo 2: ");
	scanf("%s", &e2);
	
    printf( "%s:\n", e1);
    for (i=1; i<=12; i++){
    	printf("ingrese los puntos del jugador %i: ", i);
    	scanf("%i", &p1);
    	t1+=p1;
	}
	
    printf("%s: \n", e2);
    for (j=1; j<=12; j++){
    	printf("ingrese los puntos del jugador %i: ", j);
    	scanf("%i", &p2);
    	t2+=p2;
	}	
	
	printf("los puntos de %s son: %i \n",e1, t1);
	printf("los puntos de %s son: %i \n",e2, t2);
	
	if(t1<t2)
	printf("gano: %s \n", e2);
	else if (t1=t2)
	printf ("empate \n");
	else
	printf ("gano: %s \n", e1);
	
	system ("pause");
}
