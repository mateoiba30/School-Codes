#include <fstream>
#include <iostream>
using namespace std;
int main (){
	
	char texto[128];
	ofstream archivo("archivoh.txt");
	
	if(archivo.is_open()){
		
		cout<<"ingrese un texto: "<<endl;
		cin.getline(texto, 128);
		archivo<<texto;
		
		archivo.close();
	}
	else
	cerr<<"no se pudo abrir el archivo"<<endl;
		
	return 0;
}
