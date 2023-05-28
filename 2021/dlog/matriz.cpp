#include<iostream>
using namespace std;
int main() {
	
	int matriz[3][3];
	int suma=0;
	
	for(int f=0; f<3; f++)
	for(int c=0; c<3; c++){
		cout<<"Ingrese valor, fila "<<f+1<<" columna "<<c+1<<endl;
		cin>>matriz[f][c]; 
	}
	for(int f=0; f<3; f++)
	for(int c=0; c<3; c++)
	suma+=matriz[f][c];
	
	cout<<"La suma es de: "<<suma<<endl;
	
	return 0;
}
