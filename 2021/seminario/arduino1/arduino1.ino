#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;
int main()
{
  int valor=0;
  srand(time(NULL));//esto hace que se tome un numero al azar no siempre con la misma secuencia
  for (int i=0; i<10; i++)
  {
  
  valor=rand() %100 +1;
  cout<<valor<<endl;
  }
  
  
}
