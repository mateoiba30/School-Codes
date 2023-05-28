#include <stdio.h>
// fibonacci 0 1 1 2 3 5 8 13
int main(){
	
int n, i, an, ac, f;
printf("ingrese cuantos numeros de la secuencia de fibonacci quiere ver: ");
scanf ("%i", &n);

 /*for(i=1; i<=n; i++){
 an=0;
 ac=1;
f=an+ac;
 	printf("%i, ", f);
 	ac=an;
 	an=f;
 }	
	*/ //mejor usemos un while
	i=3;//va a mostrar dos numeros mas de los que pido
	ac=0;
	an=1;	
	if (n==1)//si n=1 muestra 2 numeros (gracias a esto no)
	printf ("0, ");
	else if (n==0)
	printf ("entonces para que mierda me hiciste programar esto ? \n");
	else
	printf ("0, 1, ");
	while (i<=n){
	f=ac+an;
    printf ("%i, ", f);
    ac=an;
    an=f;
	i++;
	}
	
	system ("pause");
	return 0;
}
