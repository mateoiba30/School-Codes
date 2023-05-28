#include <iostream>
using namespace std;
int main(){
	cout<<"JUGEMOS AL AHORCADO, ADIVINA LA PALABRA (HASTA 15 INTENTOS): "<<endl;
	
    int x=0, i=0;
	char palabra[10]={'e', 's', 'c', 'a', 'l', 'o', 'f', 'r', 'i', 'o'};//ingreso al palabra directo en el código así el que juega no la puede ver
	char guiones[10]={'-', '-', '-', '-', '-', '-', '-', '-', '-', '-' };
	char letra=' ';
	
		for (int i=0; i<=9; i++)
		cout<<guiones[i]<<"  ";
		cout<<endl;
i=0;
while(x!=10 && i<=14){
	cout<<endl<<endl;
	cout<<"te quedan "<<15-i<<" intentos"<<endl;
	cout<<"ingrese una letra ==> ";
	cin>>letra;
	
	for (int i=0; i<=9; i++){
		if(letra==palabra[i]){
			guiones[i]=letra;
			x++;}
	}
	for (int i=0; i<=9; i++)
		cout<<guiones[i]<<"  ";
		cout<<endl;

i++;
	}
	cout<<endl;
	
	if(x!=10)
	cout<<"NI CON 15 INTENTOS GANAS FRACASADO"<<endl;
	else
	cout<<"MUY BIEN, FELICIDADES!!!"<<endl;
	
	return 0;
}
