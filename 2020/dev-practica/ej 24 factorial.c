#include <stdio.h>
// 5!= 1*2*3*4*5  (factorial de un numero)
int main (){
	int x, i, f=1;//f=1 porque va haber que multiplicarlo, el resto de las variables se iniciali
	printf ("introduce un numero \n");
	scanf ("%i", &x);
	
	for(i=1; i<=x; i++){//empieza en 1 y se ejecuta si i es menor o igual a x
		f=f*i;
	}
	printf ("el factorial de %i es: %i\n",x ,f);
	system ("pause");
	return 0;
}
