#include <iostream>
using namespace std;
int main ()

{
	float n1=0, n2=0, n3=0, a=0;
	cout<<"ingrese el numero 1"<<endl;
	cin>>n1;
	cout<<"ingrese el numero 2"<<endl;
	cin>>n2;
	cout<<"ingrese el numero 3"<<endl;
	cin>>n3;
	
	if(n1>n2)
{
	a=n1;
	n1=n2;
	n2=a;}
	if(n2>n3)
	{
	a=n2;
	n2=n3;
	n3=a;
	}
	cout<<n3<<endl;
	cout<<n2<<endl;
	cout<<n1<<endl;	
	
	return 0;
}
	
	

