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
    char q[1]={' '};
   
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

	cout<<"fila==> ";
	cin>>a;
	cout<<"columna==> ";
	cin>>b;	
		
    x=a-1;  	
	y=b-1;	

	system("cls");

    while (tablero [x][y]!=' '){
    cout<<"casilla ocupada!!! PRESTA ATENCION"<<endl;
	
	dibujar(tablero);
	
	cout<<"fila==> ";
	cin>>a;
	cout<<"columna==> ";
	cin>>b;	
		
    x=a-1;  	
	y=b-1;	
	
	system("cls");
	}

	if (i%2==0)
	tablero[x][y]='X';
	else
	tablero[x][y]='O';
	
    cout<<endl<<endl;
	
	for(int j=0; j<=2; j++){
	
	if(j==1)
	q[0]='X';
	else
	q[0]='O';
	
 	     if (tablero[0][0]==q[0] && tablero[0][1]==q[0] && tablero[0][2]==q[0])
	ganar=j;
	else if (tablero[1][0]==q[0] && tablero[1][1]==q[0] && tablero[1][2]==q[0])
	ganar=j;
	else if (tablero[2][0]==q[0] && tablero[2][1]==q[0] && tablero[2][2]==q[0])
	ganar=j;	
	else if (tablero[0][0]==q[0] && tablero[1][1]==q[0] && tablero[2][2]==q[0])
	ganar=j;	
	else if (tablero[0][2]==q[0] && tablero[1][1]==q[0] && tablero[2][0]==q[0])
	ganar=j;	
	else if (tablero[0][0]==q[0] && tablero[1][0]==q[0] && tablero[2][0]==q[0])
	ganar=j;
	else if (tablero[0][1]==q[0] && tablero[1][1]==q[0] && tablero[2][1]==q[0])
	ganar=j;	
	else if (tablero[0][2]==q[0] && tablero[1][2]==q[0] && tablero[2][2]==q[0])
	ganar=j;	
    }
    
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

