#include<iostream>
using namespace std;
int main() {
	
	int arreglo[5]={15, 20, 35, 4, 1};
	int may=0;
	
	for(int i=0; i<5; i++){
		if(may<arreglo[i])
		may=arreglo[i];
	}
	cout<<"El valor es: "<<may<<endl;
	
	for(int i=0; i<5; i++){
		if(arreglo[i]==may)
		cout<<"Su posicion es: "<<i<<endl;
	}
	
	return 0;
}
