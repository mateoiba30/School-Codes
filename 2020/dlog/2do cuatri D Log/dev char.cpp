//Dada una letra
#include <iostream>
using namespace std;
int main (){
	//char es para un caracter  al inicializarlo hay que dejar un espacio vacío
	//operacion de busqueda
	int encontre=0;
	char palabra[10]={'d', 'i', 'n', 'o', 's', 'a', 'u', 'r', 'i', 'o'};
	char letra=' ';
	
	cout<<"Ingrese una letra: "<<endl;
	cin>>letra;
	//Los arrays empiezan siempre en cero (0)
	for(int i=0; i<=9; i++){
		if (letra==palabra[i])
		encontre++;
	}
	cout<<"La letra "<<letra<<" se encuentra "<<encontre<<" veces "<<endl;
	
	return 0;
}
