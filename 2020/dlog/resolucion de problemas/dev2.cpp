#include <stdio.h>// todos los numeros primos entre 2 y 2000
int main (){
int i=0, j=0, s=0, m=0;// necesito asegurarme de que s no sea igual a 1 en caso de que sea primo

printf("ingrese un numero: ");
scanf("%i", &m);

	for(i=1; i<=m-1; i++){
		s=0;//necesario ya que con que una vez s valga 1 este nunca volverá a valer 0
		for(j=2; j<i && s!=1 ; j++){
			
			if (i % j==0)
			s=1;
		}
	 if (s!=1)
   	printf ("%i, ", i);//s nunca vuelve a valer 0 de no ser por la línea 9

	}
    return 0;	
}
