#include <iostream>
using namespace std;
int main()
{
	char mat [20];
	char nom [20];
	
	int n1=0, n2=0, n3=0;
	int p=0;
	
	cout<<"ingrese la materia"<<endl;
	cin>>mat;
	cout<<"ingrese su nombre"<<endl;
	cin>>nom;
	cout<<"ingrese la nota 1"<<endl;
	cin>>n1;
	cout<<"ingrese la nota 2"<<endl;
	cin>>n2;	
	cout<<"ingrese la nota 3"<<endl;
	cin>>n3;
	
	p=(n1+n2+n3)/3;
	
	if(p>=7)
	{ 
	cout<<"aprobo  "<< nom<<endl;
	cout<<mat<<" con un promedio de: "<<p;
	}
	else
		{ 
	cout<<" no aprobo  "<< nom<<endl;
	cout<<mat<<" y tuvo un promedio de: "<<p;
	}
	

	
	return 0;
	
	
	
	
}
