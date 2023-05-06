#include <stdio.h>

int main(){
	
	printf("**********************************************\n");
	printf("****** Bem vindo ao jogo de adivinhacao ******\n");
	printf("**********************************************\n");
	
	int numerosecreto = 42;
		
	int chute;
	
	printf("Qual eh o seu chute? \n");
	scanf("%d", &chute);
	
	printf("Seu chute foi %d e o numero secreto eh %d", chute, numerosecreto);
}
