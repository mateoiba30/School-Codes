#include <iostream>
using namespace std;	
int main(){
	
  float s=0;
  int v[10];
  
  for (int i=0; i<10; i++){
  v[i]=0;
    if (i%2==0)
    v[i]=i;
  }
    
  for (int i=0; i<10; i++){
  cout<<v[i]<<" ";
  }
  
   return 0;
}

