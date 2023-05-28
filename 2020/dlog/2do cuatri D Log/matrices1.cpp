#include <iostream>
using namespace std;
int main (){
	
	int matriz[3][3];
	
	for (int i=0; i<3; i++){
	for (int j=0; j<3; j++)	
	matriz[i][j]=0;}
	
	for (int k=0; k<3; k++){
	for (int l=0; l<3; l++){
    cout<<"ingrese el valor "<<k<<" "<<l<<endl;
    cin>>matriz[k][l];}}
    
    cout<<endl;

	for (int i=0; i<3; i++){
	for (int j=0; j<3; j++)	
	cout<<matriz[i][j]<<" ";}
	
	return 0;
}
