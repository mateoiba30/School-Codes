#include <fstream>
#include <iostream>
using namespace std;
int main (){
	
	string linea;
	
	ifstream archivo("archivoh.txt");
	
	if (archivo.is_open()){
		getline(archivo, linea);		
		while(!archivo.eof()){
			cout<<linea<<endl;
			getline(archivo, linea);
		}
		cout<<linea<<endl;
	}
	else
	cerr<<"error de apertura"<<endl;
	
	return 0;
}
