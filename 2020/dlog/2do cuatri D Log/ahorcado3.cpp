#include <iostream>
using namespace std;
int main(){
	cout<<"JUGEMOS AL AHORCADO, ADIVINA LA PALABRA (HASTA 10 VIDAS): "<<endl;
	cout<<"(tenes que escribir en minuscula)"<<endl;
	int v=10, f=0;
    int x=0, i=0;
	char palabra[10]={'e', 's', 'c', 'a', 'l', 'o', 'f', 'r', 'i', 'o'};//ingreso al palabra directo en el código así el que juega no la puede ver
	char guiones[10]={'-', '-', '-', '-', '-', '-', '-', '-', '-', '-' };
	char letra=' ';
	
		for (int i=0; i<=9; i++)
		cout<<guiones[i]<<"  ";
		cout<<endl;

while(x!=10 && v>0){
	f=0;
	cout<<endl<<endl;
	cout<<"te quedan "<< v <<" vidas"<<endl;
	cout<<"ingrese una letra ==> ";
	cin>>letra;
	
	for (int i=0; i<=9; i++){
		if(letra==palabra[i]){
			guiones[i]=letra;
			x++;
			f++;
			}

	}
	for (int i=0; i<=9; i++)
		cout<<guiones[i]<<"  ";
		cout<<endl;

  if(f==0)
  v=v-1;
    
	}
	cout<<endl;
	
	if(x!=10)
	cout<<"NI CON 10 VIDAS GANAS FRACASADO"<<endl;
	else
	cout<<"MUY BIEN, FELICITACIONES!!!"<<endl;
	
	return 0;
}	
