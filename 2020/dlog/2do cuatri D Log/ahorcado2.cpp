//AHORCADO 2
#include <iostream>
using namespace std;
int main (){
  
    int i=0;
	char palabra[10]={'d', 'i', 'n', 'o', 's', 'a', 'u', 'r', 'i', 'o'};//no queremos revelarle la palabra al jugador
	char guiones[10]={'_', '_', '_', '_', '_', '_', '_', '_', '_', '_'};
	char letra=' ';	
	
	for(i=0; i<=9; i++){
	cout<<guiones[i]<<" ";
	}
	cout<<endl;
	cout<<endl;
	cout<<"Ingrese una letra: "<<endl;
	cin>>letra;
	
	for(int i=0; i<=9; i++){
		if (letra==palabra[i])
		guiones[i]=letra;

	}
	for (int i=0; i<=9; i++){
		cout<<guiones[i]<<" ";
		cout<<endl;
			}	
	return 0;
}
	//que se puedan ingresar varias letras
	
