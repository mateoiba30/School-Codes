#include <iostream>
using namespace std;
int main()
{
	char mat [20];
	char nom [20];
	
	int n=0, i=0;
	int p=0;
	int s=0;
	
	cout<<"ingrese la materia"<<endl;
	cin>>mat;
	cout<<"ingrese su nombre"<<endl;
	cin>>nom;
	
	for (i=1; i<=10; i++){
	cout<<"ingrese la nota "<< i<<endl;
	cin>>n;
	s=s+n;
	}
	
	p=(s)/10;
	
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
