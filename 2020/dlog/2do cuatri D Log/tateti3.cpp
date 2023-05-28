#include <iostream>
#include<stdio.h> 
using namespace std;

void animacion1();
void animacion2 ();
void dibujar(char m[3][3]);

int main(){
	
	char tablero[3][3]={{' ', ' ', ' '},
						{' ', ' ', ' '},
						{' ', ' ', ' '}};
						
    int x=0, y=0, a=0, b=0, jx=0, jo=0, ganar=0, i=0, w=0;
   
	cout<<" __________"<<endl;
	cout<<"|          |"<<endl; 
	cout<<"| TA-TE-TI | "<<endl;
	cout<<"|__________|";
	
	i=0;
    while (i<9 && ganar==0 && y<=3){

	dibujar(tablero);
	
	if (i%2==0)
	cout<<endl<<"[turno de X]"<<endl;
	else
	cout<<endl<<"[turno de O]"<<endl;

	system("color 07");	
	cout<<"fila==> ";
	cin>>a;
	cout<<"columna==> ";
	cin>>b;	
		
    x=a-1;  	
	y=b-1;	

	system("cls");

	if(x>3 || y>3){
	cout<<"¡casilla inexistente! PRESTA ATENCION"<<endl;
	i=i-1;
}	
	
	if (tablero[x][y]=='X' || tablero[x][y]=='O' ){
	cout<<"casilla ocupada!!! PRESTA ATENCION"<<endl;
	i=i-1;
}
	if (i%2==0)
	tablero[x][y]='X';
	else
	tablero[x][y]='O';
	
    cout<<endl<<endl;
	
	if (tablero[0][0]=='X' && tablero[0][1]=='X' && tablero[0][2]=='X')
	ganar=1;
	else if (tablero[1][0]=='X' && tablero[1][1]=='X' && tablero[1][2]=='X')
	ganar=1;
	else if (tablero[2][0]=='X' && tablero[2][1]=='X' && tablero[2][2]=='X')
	ganar=1;	
	else if (tablero[0][0]=='X' && tablero[1][1]=='X' && tablero[2][2]=='X')
	ganar=1;	
	else if (tablero[0][2]=='X' && tablero[1][1]=='X' && tablero[2][0]=='X')
	ganar=1;	
	else if (tablero[0][0]=='X' && tablero[1][0]=='X' && tablero[2][0]=='X')
	ganar=1;
	else if (tablero[0][1]=='X' && tablero[1][1]=='X' && tablero[2][1]=='X')
	ganar=1;	
	else if (tablero[0][2]=='X' && tablero[1][2]=='X' && tablero[2][2]=='X')
	ganar=1;	
    else if (tablero[0][0]=='O' && tablero[0][1]=='O' && tablero[0][2]=='O')
	ganar=1;
	else if (tablero[1][0]=='O' && tablero[1][1]=='O' && tablero[1][2]=='O')
	ganar=1;
	else if (tablero[2][0]=='O' && tablero[2][1]=='O' && tablero[2][2]=='O')
	ganar=1;	
	else if (tablero[0][0]=='O' && tablero[1][1]=='O' && tablero[2][2]=='O')
	ganar=1;
	else if (tablero[0][2]=='O' && tablero[1][1]=='O' && tablero[2][0]=='O')
	ganar=1;	
	else if (tablero[0][0]=='O' && tablero[1][0]=='O' && tablero[2][0]=='O')
	ganar=1;
	else if (tablero[0][1]=='O' && tablero[1][1]=='O' && tablero[2][1]=='O')
	ganar=1;	
	else if (tablero[0][2]=='O' && tablero[1][2]=='O' && tablero[2][2]=='O')
	ganar=1;
	
	i++;
}
	if(i==9){
		system("color 06");
	cout<<"EMPATE..."<<endl<<endl;
	animacion2 ();}
	else
	if(ganar==1){
		system("color 0C");
	cout<<"El ganador es X !!!"<<endl<<endl;
	animacion1 ();	}
	else{
		system("color 09");
	
	cout<<"El ganador es O !!!"<<endl<<endl;
	animacion1 ();	}

}

	void animacion1 () {
	
	cout<<"    |  |      "<<endl;
	cout<<" |\\______/|  "<<endl;
	cout<<" \\________/   "<<endl;

	cout<<endl<<endl;
	}
	
	void animacion2 () {
	cout<<"    |  |      "<<endl;
	cout<<" __________ "<<endl;

	cout<<endl<<endl;
	}
	void dibujar(char m[3][3]){
	cout<<endl<<endl;
	
	cout<<"     |     |"<<endl;
	cout<<"   "<<m[0][0]<<" |  "<<m[0][1]<< "  |  "<<m[0][2]<<endl;
	cout<<"_____|_____|_____"<<endl;
	cout<<"     |     |"<<endl;	
	cout<<"   "<<m[1][0]<<" |  "<<m[1][1]<< "  |  "<<m[1][2]<<endl;
	cout<<"_____|_____|_____"<<endl;
	cout<<"     |     |"<<endl;	
	cout<<"   "<<m[2][0]<<" |  "<<m[2][1]<< "  |  "<<m[2][2]<<endl;
	cout<<"     |     |"<<endl;
}

