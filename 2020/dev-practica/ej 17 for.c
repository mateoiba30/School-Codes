#include <stdio.h>
 int main() {

    int   i;//el limite de un numero de int es de 32000 (aprox.)
    float c=0;//el limite de float es suficiente
    
    for(i=2; i<=2000; i=i+2){// si i es mayor a 2000 salimos// "i=i+2" == "i+=2"
    	c+=i;// == "c=c+i"
	}
    
    printf ("la suma es de: %f \n", c);//hay una f porque c esta en float
    
    system ("pause");
    return 0;

}


