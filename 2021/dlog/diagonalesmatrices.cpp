#include<iostream>
using namespace std;
int main() {
	
	int matriz[3][3];
	int sumadp=0, sumadi=0;
	
	for(int f=0; f<3; f++)
	for(int c=0; c<3; c++){
		cout<<"Ingrese valor, fila "<<f+1<<" columna "<<c+1<<endl;
		cin>>matriz[f][c]; 
	}
	for(int f=0; f<3; f++){
	sumadp+=matriz[f][f];
	sumadi+=matriz[f][2-f];
	}
	
	cout<<"La suma de la diagonal principal es de: "<<sumadp<<endl;
	cout<<"La suma de la diagonal inversa es de: "<<sumadi<<endl;	
	return 0;
}
