#include <iostream>
using namespace std;

void animacion1();
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

int main(){
	char tablero[3][3]={{' ', ' ', ' '},
						{' ', ' ', ' '},
						{' ', ' ', ' '}};
						
    int x=0, y=0, a=0, b=0, jx=0, jo=0;
   
	cout<<" __________"<<endl;
	cout<<"|          |"<<endl; 
	cout<<"| TA-TE-TI | "<<endl;
	cout<<"|__________|";
   

	dibujar(tablero);
	
    for(int i=0; i<9; i++){
	
	if(y<=3){
	
	if (i%2==0){
	cout<<endl<<"[turno de X]"<<endl;
	jx++;}
	else{
	cout<<endl<<"[turno de O]"<<endl;
	jo++;}
		
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
    if(i%2==0)
    jx--;
	else
	jo--;}	
	
	if (tablero[x][y]=='X' || tablero[x][y]=='O' ){
	cout<<"¡casilla ocupada! PRESTA ATENCION"<<endl;
	i=i-1;
    if(i%2==0)
    jx--;
	else
	jo--;}	
	else{
	if (i%2==0)
	tablero[x][y]='X';
	else
	tablero[x][y]='O';
	}
    dibujar(tablero);
    }
	
    cout<<endl<<endl;
	
/*	if(jx>jo)
	cout<<"Felicidades jugador X"<<endl;
	else
	cout<<"Felicidades jugador O"<<endl;
	animacion1 ();
	*/
}
}


/*	void animacion1 () {
	
	cout<<"    |  |      "<<endl;
	cout<<" |\\______/|  "<<endl;
	cout<<" \\________/   "<<endl;

	cout<<endl<<endl;
	}
*/
