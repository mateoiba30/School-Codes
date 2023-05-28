/*dadas 2 matrices de 4x4, calcular la suma de las 2 y cargar el resultado en una 3ra
*/
#include<iostream>
using namespace std;
int main() {
	
	int m1[4][4], m2[4][4], m3[4][4];

	for(int f=0; f<4; f++){
	for(int c=0; c<4; c++){
		cout<<"Ingrese valor, fila "<<f+1<<" columna "<<c+1<<endl;
		cin>>m1[f][c]; 
	}
}
	for(int f=0; f<4; f++){
	for(int c=0; c<4; c++){
		cout<<"Ingrese valor, fila "<<f+1<<" columna "<<c+1<<endl;
		cin>>m2[f][c]; 
	}
}
	
	for(int f=0; f<4; f++){
	for(int c=0; c<4; c++){
		m3[f][c]=m1[f][c]+m2[f][c];
	}
}

	cout<<"     |     |"<<endl;
	cout<<"   "<<m3[0][0]<<" |  "<<m3[0][1]<< "  |  "<<m3[0][2]<<endl;
	cout<<"_____|_____|_____"<<endl;
	cout<<"     |     |"<<endl;	
	cout<<"   "<<m3[1][0]<<" |  "<<m3[1][1]<< "  |  "<<m3[1][2]<<endl;
	cout<<"_____|_____|_____"<<endl;
	cout<<"     |     |"<<endl;	
	cout<<"   "<<m3[2][0]<<" |  "<<m3[2][1]<< "  |  "<<m3[2][2]<<endl;
	cout<<"     |     |"<<endl;
	return 0;
}
