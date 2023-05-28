#include <fstream>
#include <iostream>
using namespace std;
int main (){
	
	ofstream archivo("archivoh.txt");
	
	if(archivo.is_open()){
		archivo<<"sdfgfdsfgdsgsgfdgfds"<<endl;
		archivo<<"ni idea"<<endl;
		
		archivo.close();
	}
	else
	cerr<<"no se pudo abrir el archivo"<<endl;

	return 0;
}
