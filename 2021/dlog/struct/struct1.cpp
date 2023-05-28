#include <iostream>
using namespace std;

	struct alumno{
		
		string nombre;
		string apellido;
		float nota;
	};
	
	int main(){
		
		alumno a;
		cout<<"nombre: "<<endl;
		cin>>a.nombre;
		cout<<"apellido: "<<endl;
		cin>>a.apellido;
		cout<<"nota: "<<endl;
		cin>>a.nota;
		
		cout<<"Los datos ingresados son: "<<endl;
		cout<<a.nombre<<endl;
		cout<<a.apellido<<endl;
		cout<<a.nota<<endl;
						
	return 0;
}
