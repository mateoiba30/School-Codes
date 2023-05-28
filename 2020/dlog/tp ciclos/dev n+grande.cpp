#include <stdio.h>
int main()
{
	int n=0, n2=0;
	
	for(int i=1; i<=5; i++)
	{
		printf("ingrese un valor:\n");
		scanf("%i", &n);
		
		if(n<n2)
		n=n2;
	}
	
	printf("el valor mas grande es: %i", n);
	
	return 0;
	system ("pause");
}
