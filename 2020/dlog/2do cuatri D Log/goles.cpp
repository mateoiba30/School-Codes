#include <iostream>
using namespace std;
int main(){

int superanpromedio=0;
int sumagoles=0;
float promediogoles=0;	
int goles[5]={0, 0, 0, 0, 0};
string nombre[5];

for (int i=0; i<5; i++){
cout<<"JUGADOR "<<i+1<<endl;
cout<<"ingrese nombre del jugador: ";
cin>>nombre[i];
cout<<"ingrese los goles de "<<nombre[i]<<": ";
cin>>goles[i];
sumagoles=sumagoles+goles[i];
cout<<endl;
}

cout<<"El equipo anoto "<<sumagoles<<" goles"<<endl;
promediogoles=sumagoles/5;

for (int i=0; i<5; i++){
if (goles[i]>promediogoles){
superanpromedio++;
  }
}
cout<<"Hay "<<superanpromedio<<" jugadores que superan el promedio de "<<promediogoles<<" goles"<<endl;

return 0;
}
