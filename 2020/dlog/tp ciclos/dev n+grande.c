#include <iostream>
using namespace std;
int main()
{
	int n=0, n2=0, i=0;
	
	for(i=1; i<=5; i++)
	{
	cout<<"ingrese un valor: "<<endl;
	cin>>n;
		
	if(n<n2)
	n=n2;
	}
	
    cout<<"el valor mas grande es: "<<n<<endl;
	
return 0;
	system ("pause");
}
