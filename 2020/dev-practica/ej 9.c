# include <stdio.h>

int main () {
	
	int n,r;
	
	printf ("ingrese un numero entero: ");
	scanf ("%i",&n);
	
	r=n%2;
	
	if (r==0)
	printf ("es par\n");
	else
	printf ("es impar\n");
	
	system ("pause");
	return 0;
	
	
}
