#include <iostream>
using namespace std;
int main()
{
    string libros[5][3];
    cout << "Ingrese la siguiente información de los Libros: \n";
    string titulo ,autor, editorial;
    for(int i = 0; i < 5; i++)
    {
        cout << "\n-------Libro " << i + 1 << "------:\n";
        cout << "Titulo: ";
        getline(cin,titulo);
        cout << "Autor: ";
        getline(cin,autor);
        cout << "Editorial: ";
        getline(cin,editorial);      
        
		
		/*libros[i][0] = titulo;
        libros[i][1] = autor;
        libros[i][2] = editorial;   PARA QUE ES ESTO???*/
    }

    cout<<endl<<endl;
    
    system("pause");

    return 0;
}
