#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

void vidas(int x);

int main(){
	cout<<"JUGEMOS AL AHORCADO, ADIVINA LA PALABRA (HASTA 6 VIDAS): "<<endl;
	cout<<"(tenes que escribir en minuscula)"<<endl;
	int v=6, f=0, x=0, n=0;
    int i=0, j=0, k=0, h=0, p=0;
    
	char palabra[50];
	char guiones[50]={'-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-' };
	char letra=' ';

	
    printf("Ingrese la palabra: ");
	fgets(palabra, 50, stdin);
    fflush(stdin);
   
	n=strlen(palabra);
	
	system("cls");
	cout<<"JUGEMOS AL AHORCADO, ADIVINA LA PALABRA (HASTA 6 VIDAS): "<<endl;	
 	for (int j=0; j<=n-2; j++)
	cout<<guiones[j]<<"  ";
	cout<<endl;
    
    x=n-1;

while(x!=0 && v>0){
	f=0;
	cout<<endl<<endl;

	cout<<"ingrese una letra ==> ";
	cin>>letra;
	
 
    	for (k=0; k<=n; k++){
		if(letra==palabra[k]){
			guiones[k]=letra;
			f++;
			x=x-1;
			}

	}
	
	for (p=0; p<=n-2; p++)
		cout<<guiones[p]<<"  ";
		cout<<endl;

  if(f==0){
  v=v-1;
  cout<<"te quedan "<< v <<" vidas"<<endl<<endl<<endl;
  vidas(v);}    
	}
	cout<<endl;
	
	if(v<1){
	cout<<"FRACASADO"<<endl;
	cout<<"la palabra era: "<<palabra<<endl;}
	else
	cout<<"MUY BIEN, FELICITACIONES!!!"<<endl;

	return 0;
}    
void vidas(int x){
	
	switch(x){
		case 6: cout<<endl;
		
		case 5: cout<<"        O"<<endl;
		break;
		case 4: cout<<"        O"<<endl;
		        cout<<"        I"<<endl;
		break;	        
		case 3: cout<<"        O"<<endl;
		        cout<<"        I"<<endl;
		        cout<<"       /"<<endl;
     	break;		        
		case 2: cout<<"        O"<<endl;
                cout<<"        I"<<endl;
                cout<<"       / \\"<<endl;
    	break;            
		case 1: cout<<"        O"<<endl;
		        cout<<"       /I"<<endl;
		        cout<<"       / \\"<<endl;      
		break;	        
		case 0: cout<<"        O"<<endl;
		        cout<<"       /I\\"<<endl;
		        cout<<"       / \\"<<endl;    		        
		break;	
	}
	
	cout<<endl<<endl;
}
