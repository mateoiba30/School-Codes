#include<iostream>
using namespace std;
int main() {
	
	int matriz[3][3];
	int suma[3];
	float prom[3];
	
	for(int f=0; f<3; f++){
	suma[f]=0;
	for(int c=0; c<3; c++){
		cout<<"Ingrese valor, fila "<<f+1<<" columna "<<c+1<<endl;
		cin>>matriz[f][c]; 
		
		suma[f]+=matriz[f][c];
	}
}
    cout<<endl;
    
	prom[0]=suma[0]/3;
	cout<<"El promedio de la fila 1 es de: "<<prom[0]<<endl;
	
	prom[1]=suma[1]/3;
	cout<<"El promedio de la fila 2 es de: "<<prom[1]<<endl;
	
	prom[2]=suma[2]/3;
	cout<<"El promedio de la fila 3 es de: "<<prom[2]<<endl;
	
	return 0;
}
