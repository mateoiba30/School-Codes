#include <iostream>
using namespace std;

	struct alumno{
		
		string nombre;
		string apellido;
		float nota;
	};
	
	int main(){
	
	float maynota=0;
	int pos=0;
	alumno a[10];
	
	for (int i=0; i<10; i++){
		cout<<"nombre: "<<endl;
		cin>>a[i].nombre;
		cout<<"apellido: "<<endl;
		cin>>a[i].apellido;
		cout<<"nota: "<<endl;
		cin>>a[i].nota;
	}
	for(int i=0; i<10; i++){
		if(a[i].nota>maynota){
			maynota=a[i].nota;
			pos=i;
		}
	}
	
	cout<<"---------------------------------------------------------------------"<<endl;
	
	cout<<"el alumno con mayor nota es: "<<endl;
	cout<<a[pos].nombre;
	cout<<"  ";
	cout<<a[pos].apellido<<endl;
	cout<<"con una nota de: ";
	cout<<a[pos].nota<<endl;
					
	return 0;
}
