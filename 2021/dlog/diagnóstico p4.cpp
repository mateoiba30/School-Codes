#include <iostream>
using namespace std;
int main (){
	
	int i=0, m=0, g=0, mayor=0;
	
	for (i=0; i<12; i++){
    cout<<"Ingrese cuantos pesos gano en el mes "<<i+1<<": "<<endl;
    cin>>g;
    
    if (g>mayor){
    mayor=g;
    m=i+1;}
    
}
	cout<<"El mes en el que mas gano fue el "<<m<<", con un total de $"<<mayor<<endl;
	
	return 0;
}
