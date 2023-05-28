#include <stdio.h>
// introduce  un horario y yo le sumo 1 segundo
int main () {
	
	int h, m, s;
	
	printf ("ingrese las horas: ");
	scanf ("%i", &h);
	printf ("ingrese los minutos: ");
	scanf ("%i", &m);
	printf ("ingrese los segundos: ");
	scanf ("%i", &s);
	
	if (h<=23 && m<=59 && s<=59){// se puede hacer con un switch, pero es lo mismo
	s++;// es lo mismo que poner s+=1 o s=s+1
	if (s==60){
	m++;
	s=0;}
    if (m==60){
	
	h++;
	m=0;}
	if (h==24)
	h=0;
	printf ("la hora es %i:%i:%i \n\n",h,m,s);}
	else
	printf ("la hora introducida es incorrecta\n\n");
	
	

	
	system ("pause");
	return 0;
}
