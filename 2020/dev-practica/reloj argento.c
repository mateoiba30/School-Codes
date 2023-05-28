#include <stdio.h>
#include <windows.h>
int main (){
	
	int h=0, s=0, min=0, x=0;
	char m[10];
	
    x=1;

	for(h=0; h<24; h++){
		for(min=0; min<60; min++){
			for(s=0; s<60; s++){
				
		
		if(min==0){
		
		m[10]='en-punto';
		printf ("%02i:%s \r",h, m);}
		
		else if (min==15){	
	
		m[10]='y-cuarto';
		printf ("%02i:%s \r",h, m);}
		
		else if (min==30){
      
        m[10]='y-media';
		printf ("%02i:%s \r",h, m);}
        
        else if (min==45){
	
		h+=1;
		m[10]='menos-cuarto';
		printf ("%02i:%s \r",h, m); }
		
		else
			
			printf ("%02i:%02i:%02i \r",h, min, s);
			Sleep (x);
		}
	}
}

//el programa termina en 1 día
system ("pause");
return 0;

}
