#include <stdio.h>
#include <windows.h>//libreria para el cronometro, si sos de windows
int main (){
	
	int h, m, s, x;
	
/*	for(h=0; h<24; h++){
		printf ("%i:",h);
		for(m=0; m<60; m++){
			printf ("%i:",m);
			for(s=0; s<60; s++){
				printf ("%i:",s);
			
		}
	}
}
*/ //así va solo a contar y mostrar un monton de numeros
x=1000;

//el Sleep hace que nuestro programa se duerma por un tiempo (en miliseg.) para que no cuente a mil por hora
	for(h=0; h<24; h++){
	
		for(m=0; m<60; m++){
		
			for(s=0; s<60; s++){//no poner s<=60
				printf ("%02i:%02i:%02i \r",h,m,s);//puse un 02 para que aparezaca al menos dos números// puse la r y no la n, porque sobreescrive el mensaje (borra lo anterior
			Sleep (x);//la S en mayuscula
		}//como la función usleep se cuentan micro segundos. seria: usleep(1000*x);
	}
}

//el programa termina en 1 día
system ("pause");
return 0;

}
