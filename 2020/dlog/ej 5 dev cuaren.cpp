#include <iostream>
using namespace std;
int main ()
{

int n1=0, n2=0, d=0;
cout<<"ingrese un numero"<<endl;
cin>>n1;
cout<<"ingrese otro numeero"<<endl;
cin>>n2;

  if(n2==0)
  cout<<"imposible dividir por cero";
  
  else
  {
  d=n1/n2;
  cout<<"el resultado es de: "<<d<<endl;
}
return 0;
}
