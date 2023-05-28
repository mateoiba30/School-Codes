#include <stdio.h>
int main (){
	
	double a=0, b=0, i=0, s=0;
	
	a=0;
	b=1;
	
	for(i=1; i<=178; i++){ //cuando uso terminos más chicos anda igual que en pseint, quizá que el "int" no acepta un numero tan grande
		s=a+b;
		a=b;// el termino 180 es 11463113765491467695340528626429782121, pero es muy grande
		b=s;
	}
	
	printf("el termino 180 de la secuencia de fibonacci es %i \n",b);
	
	return 0;
}
