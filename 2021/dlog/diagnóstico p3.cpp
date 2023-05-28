#include <iostream>
#include <math.h>
using namespace std;
int main ()

{
	int y=0, x=0;
    for ( x=-1000; x<=1000; x++){
    
	y=pow((-3*x), 3) + pow((2*x), 2) - 3*x +10;
	
	if (y % 2 == 0){
	cout<<"x="<<x<<endl;
	cout<<"y="<<y<<endl;
	cout<<endl;
	}
}
	
	return 0;
	
}
